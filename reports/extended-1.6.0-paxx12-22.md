# Extended 1.6.0-paxx12-22 Türkçe — Derleme raporu

## Kaynak ve çıktı

- Kaynak: [paxx12-snapmaker-u1/SnapmakerU1-Extended-Firmware v1.6.0-paxx12-22](https://github.com/paxx12-snapmaker-u1/SnapmakerU1-Extended-Firmware/releases/tag/v1.6.0-paxx12-22)
- Kaynak yayın 9 Eylül 2026 kontrolünde **Pre-release** durumundadır.
- Kaynak dosya: `U1_extended_1.6.0-paxx12-22_upgrade.bin`
- Kaynak boyutu: `247180032` bayt
- Kaynak SHA-256: `EEA907C22847B6F165640F0AE5E835CA42181F7A39B722FF062FD138D47A689C`
- Çıktı: `TURKISH_QUINRY_U1_extended_1.6.0-paxx12-22_upgrade.bin`
- Çıktı boyutu: `247270144` bayt
- Çıktı SHA-256: `812A9496460715DB94456D2B1FD68436C158206E42A03BB5369E16301884E3B6`
- Korunan UPFILE sürümü: `1.6.0.26731c5a38`
- Korunan UPFILE tarihi: `20260815150420`

## Çeviri kaynağı

Kaynak paket ayrı bir klasöre açıldı. Yeni firmware'den altı dilin 550 ana arayüz ve 458 hata kaydı çıkarıldı. GUI'nin Stock 1.6.0.267 kaynak GUI'siyle bayt bayt aynı olduğu doğrulandı. 1008 İngilizce kaydın tamamı da anahtar ve değer bazında aynı bulundu. Önceki Türkçe karşılıklar yalnız bu eşleşmeler doğrulandıktan sonra kullanıldı; yeni veya değişmiş İngilizce kayıt bulunmadı.

Türkçe, altı mevcut dil korunarak yedinci `tr-TR` seçeneği olarak eklendi. Dosyalar UTF-8, NFC ve BOM'suzdur. Anahtar sırası, yer tutucular, sayılar, satır sonları, biçimlendirme ve hata başlık/gövde ayraçları doğrulandı. Yeni firmware'deki HarmonyOS ve Roboto arayüz fontları Türkçe karakterlerin tamamını kapsıyor.

- Ana metin SHA-256: `B4AA86B72C88CEB35A7600C96E0F343904006A0A82E79EFA8C5B9888E1D187EC`
- Hata metni SHA-256: `81D1FFF203CB79B08917C16FBFF1715C063019461156473296F7A964B7A912FD`
- Yamalı GUI SHA-256: `DF70EE929F80FDBBBA2F0F5348DBC38A6F30533756E73F40CB235352AB16D48B`

## Paketleme

- SquashFS 4.0, Zstandard, 131072 bayt blok boyutu ve kaynak dosya sistemi tarihi `1788809243` korundu.
- Rootfs boyutu `207745024` bayt; bölüm sınırı `314572800` bayt.
- Rootfs SHA-256: `C71828B0FDD735E2CEF5F6557287DD0C77D7E8DD6A40A0D815DF0611EC6E538C`
- RKAF SHA-256: `8F0E90A35BB0B1ECB1DE4643C58D1D6D8FBD8746BC91B008B3FEA67E6A8BB37E`
- RKFW SHA-256: `816655B7A34BC2741E2036B43F167500F5AD6388AF46403A67A3A8F8422AFCEF`
- Kaynakta xattr bulunmuyor. Daha önce kullanılan squashfs-tools-ng aracının bilgilendirme bayrakları `0x00c0 → 0x02e0` değişiyor (`ALWAYS_FRAGMENTS` ve `NO_XATTRS`); dosya içerikleri ve metaverileri ayrıca karşılaştırıldı.

## Son doğrulama

Final `.bin` UPFILE → RKFW → RKAF → SquashFS katmanlarıyla yeniden açıldı. UPFILE checksum/MD5, RKFW MD5, RKAF CRC, paket başlıkları ve bölüm yerleşimi kontrolleri geçti.

Kaynak dosya sistemindeki 13.351 TAR girdisinin içerikleri ve metaverileri yeniden açılan çıktıyla karşılaştırıldı. Yalnız `/usr/bin/gui` değişti; `/home/lava/resource/text/exception_tr-TR.json` eklendi. Mevcut dosyaların sahiplikleri, izinleri, zamanları ve bağlantıları korundu. MCU, loader ve rootfs dışındaki tüm bölümler yeni kaynakla aynıdır.

Son paketten çıkarılan GUI ve Türkçe hata dosyası beklenen dosyalarla birebir eşleşti. GUI **80/80 PASS** aldı; AArch64 yürütme denetimi Türkçe dil kaydı, seçim, enum 6, metin arama, kalıcı ayar ve Türkçe hata dosyası yolunu doğruladı.

Bu yeni Extended 1.6.0-paxx12-22 Türkçe dosyası için fiziksel yazıcıda yükleme/açılış testi henüz bildirilmedi.
