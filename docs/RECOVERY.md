# Recovery guidance

Modified firmware always carries risk. Prepare the official firmware for the exact printer model before updating and keep the printer connected to stable power.

## If the touchscreen still works

1. Download the correct official Snapmaker U1 firmware from Snapmaker's official support source.
2. Verify that the download is intended for the U1 and is not an Extended build.
3. Copy only the official update file to a FAT32 or exFAT USB drive.
4. Open **Settings → About**, tap **Firmware Version**, choose **Local Update** in the top-right corner, select the verified official file, and do not interrupt power during the update.
5. After boot, confirm the reported version and review printer settings before starting a print.

## If the touchscreen update path is unavailable

Stop experimenting with unrelated images, partition layouts, bootloaders or low-level flashing commands. Record the exact firmware filename, SHA-256, symptoms and any messages shown, then contact Snapmaker support or an experienced U1 firmware maintainer.

Low-level recovery procedures can permanently overwrite boot or calibration data and are intentionally not provided here without a verified device-specific recovery path.

## Report useful diagnostics

When opening an issue, include:

- printer model;
- Stock or Extended channel;
- exact base and Turkish release tag;
- downloaded filename and SHA-256;
- whether flashing completed;
- whether the display, network and motion controller start;
- a photo of the visible error, with personal information removed.
