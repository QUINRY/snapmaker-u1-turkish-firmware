# Snapmaker U1 1.6.0 Türkçe firmware derleme raporu

## Çıktı

- Firmware: `U1_1.6.0.267_20260815150420_TR_upgrade.bin`
- Boyut: `279016192` bayt
- SHA-256: `A8483C8B9909FC527904461F8521FA7D4D91780FC718343C6C89E7999D5197E5`
- UPFILE sürümü: `1.6.0.267`
- UPFILE derleme tarihi: `20260815150420`

Kaynak firmware değiştirilmedi:

- Kaynak: `U1_1.6.0.267_20260815150420_upgrade.bin`
- Boyut: `254649088` bayt
- SHA-256: `9F446819E51A2E7A2F0516FDE0C025F2B1CD9C23396301E0F5C45E7859CD8AF4`

## Türkçe içerik

- Yalnızca resmi 1.6.0 İngilizce kaynakları esas alındı; eski 1.5.2 çeviri içeriği kullanılmadı.
- Mevcut altı dil korunarak yedinci dil olarak `tr-TR` / `Türkçe` eklendi.
- Ana arayüz: `550/550` kayıt, UTF-8 ve NFC.
- Hata kataloğu: `458/458` kayıt, UTF-8 ve NFC.
- `main.json` SHA-256: `B4AA86B72C88CEB35A7600C96E0F343904006A0A82E79EFA8C5B9888E1D187EC`
- `errors.json` SHA-256: `81D1FFF203CB79B08917C16FBFF1715C063019461156473296F7A964B7A912FD`
- GUI içinde dil kaydı, seçim, enum `6`, kalıcı ayar ve metin arama yolları eklendi.
- 1.6.0'ın harici hata kataloğu düzenine uygun olarak `/home/lava/resource/text/exception_tr-TR.json` eklendi.
- GUI SHA-256: `DF70EE929F80FDBBBA2F0F5348DBC38A6F30533756E73F40CB235352AB16D48B`

## Paketleme

- SquashFS `4.0`, LZ4, `65536` bayt blok boyutu kullanıldı.
- Türkçe rootfs boyutu `239489024` bayt; `314572800` baytlık bölüm sınırında `75083776` bayt boşluk kaldı.
- Windows için squashfs-tools-ng 1.3.2'nin LZ4 `hc` seçeneği erişim ihlaliyle kapanmaktadır; bu davranış [upstream issue #134](https://github.com/AgentD/squashfs-tools-ng/issues/134) ile aynıdır. Bu nedenle aynı LZ4 disk biçimi normal sıkıştırma kipinde üretildi.
- Rootfs SHA-256: `84F998D3EA3BB814660252AB25A58196DC84E17CC16A18EDAF2E68AE802C221E`
- RKAF SHA-256: `0C7BF48B0FB0800EE711FBEE75B398DFEC281F6CC06B036D53047792EA01D727`
- RKFW SHA-256: `7C88EFA5BC725B9922EF2F84C7B3B39085E78775A728374FD2E231FBFD2B98B5`

## Doğrulama

- UPFILE başlık checksum'u ve dört girdi MD5'i geçti.
- RKFW sonundaki ASCII MD5 geçti: `105a1dd8228c74135b77fb26daa63837`.
- RKAF CRC kontrolü geçti.
- Final `.bin`, ayrı bir klasöre UPFILE → RKFW → RKAF → SquashFS olarak sıfırdan yeniden açıldı.
- MCU1, MCU2, MCU tanımı, loader, boot, U-Boot, misc, OEM ve userdata kaynak 1.6.0 ile byte-for-byte aynıdır.
- Final rootfs içinden çıkarılan GUI ve `exception_tr-TR.json`, beklenen dosyalarla byte-for-byte aynıdır.
- Final GUI bağımsız doğrulamada `80/80 PASS` aldı. AArch64 sembolik yürütmede Türkçe kayıt/seçim, enum, metin arama, kalıcı kayıt ve hata kataloğu yönlendirme yolları geçti.
- SquashFS içerik/tarih karşılaştırması yalnız yeni Türkçe hata dosyasını ve değiştirilmiş GUI'yi raporladı. Araç ayrıca iki değişmemiş dosyayı seyrek blok algılaması nedeniyle `extended inode` olarak gösterdi; iki dosyanın kaynak ve final SHA-256 değerleri birebir aynıdır.
- Türkçe font glif kapsamı ve uzun açıklamaların piksel genişlikleri denetlendi.
- Fiziksel yazıcıya flash testi yapılmadı.
