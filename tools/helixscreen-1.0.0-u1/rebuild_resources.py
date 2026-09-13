#!/usr/bin/env python3
"""Rebuild the HelixScreen 1.0.0 U1 Turkish XML overlay from pinned originals."""
from __future__ import annotations

import argparse
from collections import Counter
import copy
import hashlib
from io import BytesIO
import json
from pathlib import Path
import re
import unicodedata
import xml.etree.ElementTree as ET

SOURCE_HASHES = {
    "bin/helix-screen": "e570921f12b94174dc3cea8063ec44b2a645e32a6d133e482d5fab4da04c19ae",
    "ui_xml/translations/en.xml": "509aceca57469a5bc00d0675e0b3182a7d62426596700686f940aadc5f6dde61",
    "ui_xml/translations/translations.xml": "128611771c8bdd73717ec5f30996cb3376119e2b73087b2de06829d5a1a2153d",
    "ui_xml/wizard_language_chooser.xml": "0860c10bb599b30a6742da4f9068786541224e518720a5ba2955033b43b68f45",
}
APPROVED_TR_SHA256 = "e7594151ea7f710474f13797b0b03eaf3bc62b4219beeee3ff832ab81849843d"
APPROVED_OUTPUT_HASHES = {
    "ui_xml/translations/tr.xml": APPROVED_TR_SHA256,
    "ui_xml/translations/translations.xml": "07c39784d7c1b7dd73ee4d9705b20462436d0be5b7f3f083ea6d5724aef0f108",
    "ui_xml/wizard_language_chooser.xml": "9780f119603e324d6d781562ab114da7d314734fc78992f8e9635c924f8efecd",
}
ORIGINAL_LANGUAGES = ["de", "en", "es", "fr", "it", "ja", "pt", "ru", "zh"]
WIZARD_LANGUAGES = ["en", "de", "fr", "es", "ru", "pt", "it", "zh", "ja"]
PRINTF = re.compile(r"%(?:\d+\$)?[-+0 #]*\d*(?:\.\d+)?(?:hh|h|ll|l|z|t|j)?[diuoxXfFeEgGaAcspn%]")
FMT = re.compile(r"\{[^{}]*\}")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def parse_catalogue(data, language):
    require(not data.startswith(b"\xef\xbb\xbf"), "UTF-8 BOM is not supported")
    root = ET.fromstring(data.decode("utf-8", errors="strict"))
    require(root.tag == "translations", "Unexpected catalogue root")
    values = {}
    for row in root:
        require(row.tag == "translation", "Unexpected catalogue element")
        key = row.attrib["tag"]
        require(key not in values, "Duplicate translation key: " + key)
        values[key] = row.attrib[language]
    return root, values


def xml_bytes(root):
    buffer = BytesIO()
    ET.ElementTree(root).write(buffer, encoding="utf-8", xml_declaration=True,
                               short_empty_elements=True)
    # The approved Windows build used CRLF after the XML declaration. Fix the
    # serialization explicitly so Linux and Windows reproduce identical bytes.
    return buffer.getvalue().replace(b"\n", b"\r\n")


def validate_translations(english, turkish):
    require(list(english) == list(turkish), "Turkish keys/order differ from current English")
    for key, source in english.items():
        text = turkish[key]
        require(bool(source) == bool(text), "Empty-value mismatch: " + key)
        require(unicodedata.is_normalized("NFC", text), "Non-NFC text: " + key)
        require(not any(c in text for c in ("\x00", "\ufffd")), "Invalid text: " + key)
        before, after = PRINTF.findall(source), PRINTF.findall(text)
        require(Counter(before) == Counter(after), "Printf token mismatch: " + key)
        if not all(re.match(r"%\d+\$", token) or token == "%%" for token in before):
            require(before == after, "Printf argument-order mismatch: " + key)
        require(FMT.findall(source) == FMT.findall(text), "Format argument mismatch: " + key)
        require(Counter(re.findall(r"\$\d+", source)) == Counter(re.findall(r"\$\d+", text)),
                "Dollar placeholder mismatch: " + key)
        require(source.count("\n") == text.count("\n"), "Newline mismatch: " + key)
        def numbers(value):
            value = FMT.sub("", PRINTF.sub("", value))
            return Counter(item.replace(",", ".") for item in re.findall(r"\d+(?:[.,]\d+)?", value))
        require(numbers(source) == numbers(text), "Numeric value mismatch: " + key)


def rebuild(official_root, translation, output):
    official_root = official_root.resolve(strict=True)
    translation = translation.resolve(strict=True)
    output = output.resolve()
    require(official_root.is_dir(), "Official root must be the extracted helixscreen directory")
    require(not output.is_relative_to(official_root) and not official_root.is_relative_to(output),
            "Output and official root must be separate, non-overlapping directories")
    require(not translation.is_relative_to(output), "Input translation must be outside the output")
    sources = {name: (official_root / name).read_bytes() for name in SOURCE_HASHES}
    for name, expected in SOURCE_HASHES.items():
        require(digest(sources[name]) == expected, "Wrong official 1.0.0 U1 source: " + name)
    tr_bytes = translation.read_bytes()
    tr_root, turkish = parse_catalogue(tr_bytes, "tr")
    require(tr_root.attrib.get("languages") == "tr", "Translation must declare languages=tr")
    _, english = parse_catalogue(sources["ui_xml/translations/en.xml"], "en")
    combined, combined_en = parse_catalogue(sources["ui_xml/translations/translations.xml"], "en")
    require(len(english) == 2868 and english == combined_en, "Current English catalogue mismatch")
    validate_translations(english, turkish)
    require(combined.attrib.get("languages", "").split() == ORIGINAL_LANGUAGES,
            "Original language list differs")
    merged = copy.deepcopy(combined)
    merged.set("languages", " ".join([*ORIGINAL_LANGUAGES, "tr"]))
    for row in merged:
        row.set("tr", turkish[row.attrib["tag"]])
    for before, after in zip(combined, merged, strict=True):
        require({key: value for key, value in after.attrib.items() if key != "tr"} == before.attrib,
                "An original language value changed")

    wizard = ET.fromstring(sources["ui_xml/wizard_language_chooser.xml"].decode("utf-8"))
    lists = [node for node in wizard.iter("lv_obj") if node.attrib.get("name") == "language_list"]
    require(len(lists) == 1 and len(lists[0]) == 9, "Unexpected wizard language list")
    parent = lists[0]
    original_rows = [ET.tostring(row) for row in parent]
    for index, (row, code) in enumerate(zip(parent, WIZARD_LANGUAGES, strict=True)):
        require(row.tag == "lv_button" and row.attrib.get("name") == "lang_item_" + code,
                "Unexpected wizard language row")
        require(row.find("event_cb").attrib == {"trigger": "clicked", "callback": "on_language_selected", "user_data": str(index)},
                "Unexpected wizard callback")
    row = copy.deepcopy(parent[-1])
    row.set("name", "lang_item_tr")
    row.find("text_body").set("text", "Türkçe")
    row.find("event_cb").set("user_data", "9")
    for icon in row.findall("lv_image"):
        row.remove(icon)
    parent.append(row)
    require([ET.tostring(row) for row in list(parent)[:9]] == original_rows,
            "An original wizard row changed")
    outputs = {
        "ui_xml/translations/tr.xml": xml_bytes(tr_root),
        "ui_xml/translations/translations.xml": xml_bytes(merged),
        "ui_xml/wizard_language_chooser.xml": xml_bytes(wizard),
    }
    hashes = {name: digest(data) for name, data in outputs.items()}
    if hashes["ui_xml/translations/tr.xml"] == APPROVED_TR_SHA256:
        require(hashes == APPROVED_OUTPUT_HASHES, "Approved release resource reproduction mismatch: " + repr(hashes))
    report = {
        "version": "1.0.0", "platform": "snapmaker-u1", "passed": True,
        "source_sha256": SOURCE_HASHES, "translation_sha256": digest(tr_bytes),
        "english_count": len(english), "turkish_count": len(turkish),
        "existing_languages_preserved": ORIGINAL_LANGUAGES,
        "existing_wizard_rows_preserved": 9, "turkish_wizard_index": 9,
        "output_sha256": hashes,
        "matches_approved_release": hashes == APPROVED_OUTPUT_HASHES,
    }
    outputs["resource_rebuild_report.json"] = (json.dumps(report, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    # Preflight all destinations before writing. Identical reruns are allowed;
    # unrelated or modified output files are never overwritten.
    for name, data in outputs.items():
        destination = output / name
        require(destination.resolve().is_relative_to(output), "Output symlink escapes its directory")
        require(not destination.exists() or destination.read_bytes() == data,
                "Refusing to overwrite a different output file: " + str(destination))
    for name, data in outputs.items():
        destination = output / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        if not destination.exists():
            destination.write_bytes(data)
    for name, expected in SOURCE_HASHES.items():
        require(digest((official_root / name).read_bytes()) == expected, "Official source changed")
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--official-root", type=Path, required=True)
    parser.add_argument("--translation", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(rebuild(args.official_root, args.translation, args.output), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
