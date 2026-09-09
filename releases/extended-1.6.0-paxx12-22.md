# Snapmaker U1 Extended 1.6.0-paxx12-22 — Türkçe

Snapmaker U1 dokunmatik ekranına Türkçe ekleyen, **Extended 1.6.0-paxx12-22** tabanlı firmware paketidir. Mevcut altı dil korunur; Türkçe ayrı bir `tr-TR` seçeneği olarak eklenir. Ücretsiz, kâr amacı gütmeyen ve resmî olmayan bir topluluk çalışmasıdır.

> **Kaynak / Credits:** Extended firmware, [paxx12-snapmaker-u1/SnapmakerU1-Extended-Firmware](https://github.com/paxx12-snapmaker-u1/SnapmakerU1-Extended-Firmware/releases/tag/v1.6.0-paxx12-22) projesinin çalışmasıdır. Geliştiricilerine ve katkıda bulunanlara teşekkürler. Kaynak yayın ön sürüm olduğu için bu Türkçe yayın da **Pre-release** olarak sunulmaktadır.

## Hızlı kurulum

1. Aşağıdaki **Assets** bölümünden `TURKISH_QUINRY_U1_extended_1.6.0-paxx12-22_upgrade.bin` dosyasını indirin; SHA-256 değerini doğrulayın.
2. `.bin` dosyasını **FAT32** USB belleğin kök dizinine kopyalayıp belleği yazıcıya takın.
3. Yazıcıda **Settings → About → Firmware Version → Local Update** yolunu açın.
4. Dosyayı seçip güncellemeyi onaylayın. Güncelleme tamamlanıp yazıcı açılana kadar gücü kesmeyin ve belleği çıkarmayın.
5. Dil ayarlarından **Türkçe** seçin.

Menü adları, Türkçe kurulmadan önce yazıcıda görülen İngilizce biçimiyle verilmiştir. [Resimli kurulum anlatımı](https://github.com/QUINRY/snapmaker-u1-turkish-firmware#h%C4%B1zl%C4%B1-kurulum) · [SHA-256 doğrulama rehberi](https://github.com/QUINRY/snapmaker-u1-turkish-firmware/blob/main/docs/VERIFY.md)

## Dosya bilgileri

- Hedef sürüm: **Extended 1.6.0-paxx12-22**
- Dosya: `TURKISH_QUINRY_U1_extended_1.6.0-paxx12-22_upgrade.bin`
- Boyut: `247270144` bayt (yaklaşık 247 MB)
- SHA-256: `812A9496460715DB94456D2B1FD68436C158206E42A03BB5369E16301884E3B6`
- Kaynak dosya: `U1_extended_1.6.0-paxx12-22_upgrade.bin`
- Kaynak SHA-256: `EEA907C22847B6F165640F0AE5E835CA42181F7A39B722FF062FD138D47A689C`
- Korunan UPFILE sürümü/tarihi: `1.6.0.26731c5a38` / `20260815150420`

Assets içindeki `.bin` flashlanacak tam firmware dosyasıdır. `.sha256`, `.json` ve `.md` dosyaları doğrulama bilgilerini ve teknik raporu içerir.

## Türkçe içerik ve doğrulama

- 550 arayüz metni ve 458 hata kaydı; Türkçe karakterli UTF-8, NFC ve BOM'suz JSON.
- İngilizce metinler bu yeni firmware'den çıkarıldı. 1008 kaydın anahtar ve değerleri önceki Stock 1.6.0.267 kaynaklarıyla birebir eşleştiği doğrulandıktan sonra mevcut Türkçe çeviriler kullanıldı.
- Yer tutucular, sayısal değerler, satır sonları ve anahtar sırası doğrulandı. Yeni paketin ana arayüz fontlarında Türkçe karakter kapsamı kontrol edildi.
- Final firmware yeniden açıldı; UPFILE checksum/MD5, RKAF CRC ve RKFW MD5 kontrolleri geçti.
- Dosya sistemi karşılaştırmasında yalnız `/usr/bin/gui` değişti ve `exception_tr-TR.json` eklendi. Diğer dosyalar, izinler, MCU, loader ve rootfs dışındaki bölümler korundu.
- Yeni kaynağın Zstandard sıkıştırması, 131072 bayt blok boyutu ve dosya sistemi tarihi korundu.
- Final paketten çıkarılan ekran uygulaması, AArch64 yürütme kontrolleri dahil **80/80 PASS** aldı.

## Fiziksel test durumu

Bu **Extended 1.6.0-paxx12-22 Türkçe** dosyası için fiziksel yazıcıda yükleme/açılış testi henüz bildirilmedi. Önceki sürümlerde belgelenen başarılı kurulum zinciri bu yeni dosyaya ait test kaydı değildir. Yazılımsal doğrulama sonuçları yukarıda ve ekli teknik raporda yer alır.

## Lisans

Bu projenin özgün çeviri, araç ve belgeleri `GPL-3.0-only` kapsamındadır. Snapmaker ve Extended Firmware bileşenleri kendi lisans ve telif koşullarına tabidir. Bu Türkçe çalışma Snapmaker veya Extended Firmware geliştiricileri tarafından onaylanmış ya da desteklenmiş değildir.
