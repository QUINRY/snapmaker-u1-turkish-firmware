# Turkish translation sources

The versioned directories contain only the reviewed Turkish localization tables used for each exact base firmware.

- `stock/1.6.0.267/tr-TR`
- `extended/1.5.2-paxx12-21/tr-TR`
- `extended/1.4.1-paxx12-20/tr-TR`

Translations are intentionally kept separate because message keys and meanings change between firmware versions. Never merge or copy a table into a different base version without extracting and reviewing that version's own English source.

The JSON files are UTF-8 without BOM and use NFC-normalized Turkish characters. Values such as placeholders, model identifiers, URLs, technical tokens and intentional line breaks must be preserved when editing.

These files do not grant a license to third-party firmware or interface components. See [NOTICE.md](../NOTICE.md) and [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md).
