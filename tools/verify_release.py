#!/usr/bin/env python3
"""Verify a firmware release asset against this repository's manifest."""

# Copyright (C) 2026 QUINRY
# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Verify a Snapmaker U1 Turkish firmware release asset."
    )
    parser.add_argument("manifest", type=Path, help="Version manifest JSON file")
    parser.add_argument("firmware", type=Path, help="Downloaded firmware .bin file")
    return parser.parse_args()


def load_manifest(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8-sig") as handle:
        manifest = json.load(handle)
    asset = manifest.get("release_asset")
    if not isinstance(asset, dict):
        raise ValueError("Manifest does not contain a release_asset object")
    for key in ("filename", "size_bytes", "sha256"):
        if key not in asset:
            raise ValueError(f"Manifest release_asset is missing {key!r}")
    return manifest


def calculate_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def main() -> int:
    args = parse_args()
    manifest = load_manifest(args.manifest)
    expected = manifest["release_asset"]

    if not args.firmware.is_file():
        print(f"FAIL: file not found: {args.firmware}")
        return 2

    failures: list[str] = []
    expected_name = str(expected["filename"])
    expected_size = int(expected["size_bytes"])
    expected_hash = str(expected["sha256"]).upper()

    if args.firmware.name != expected_name:
        failures.append(
            f"filename mismatch: expected {expected_name!r}, got {args.firmware.name!r}"
        )

    actual_size = args.firmware.stat().st_size
    if actual_size != expected_size:
        failures.append(
            f"size mismatch: expected {expected_size}, got {actual_size} bytes"
        )

    actual_hash = calculate_sha256(args.firmware)
    if actual_hash != expected_hash:
        failures.append(
            f"SHA-256 mismatch: expected {expected_hash}, got {actual_hash}"
        )

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print(f"PASS: {args.firmware.name}")
    print(f"Size: {actual_size} bytes")
    print(f"SHA-256: {actual_hash}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
