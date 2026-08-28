# Snapmaker U1 Extended 1.4.1-paxx12-20 — Türkçe

Bu paket, Snapmaker U1 için **Extended 1.4.1-paxx12-20** firmware'i temel alınarak hazırlanmış Türkçe yerelleştirmedir. Ücretsiz, kâr amacı gütmeyen ve resmî olmayan bir topluluk çalışmasıdır; Snapmaker veya Extended Firmware geliştiricileri tarafından desteklenmiş ya da onaylanmış değildir.

> **Kaynak / Credits:** Bu paketin Extended tabanı [paxx12-snapmaker-u1/SnapmakerU1-Extended-Firmware](https://github.com/paxx12-snapmaker-u1/SnapmakerU1-Extended-Firmware) projesi tarafından yayımlanmıştır. Özgün Extended Firmware geliştirmesi ve yayını için kaynak projenin bakımcılarına ve katkıda bulunanlarına teşekkür ederiz.

## Hızlı kurulum

> Türkçe firmware henüz kurulmadığı için menü adları yazıcıda göründüğü İngilizce biçimiyle verilmiştir.

1. Bu release'teki `.bin` dosyasını indirin ve aşağıdaki tam SHA-256 değeriyle doğrulayın.
2. Dosyayı **FAT32** biçimli USB belleğin kök dizinine kopyalayın. Bellekte yalnızca yükleyeceğiniz tek firmware `.bin` dosyasını bırakın ve belleği yazıcıya takın.
3. Dokunmatik ekranda **Settings → About** bölümünü açıp **Firmware Version** satırına dokunun.
4. Sağ üstteki **Local Update** seçeneğine girin.
5. USB bellekteki `.bin` dosyasını seçip güncellemeyi onaylayın.
6. Güncelleme tamamlanıp yazıcı yeniden başlayana kadar gücü kesmeyin ve USB belleği çıkarmayın.
7. Yeniden başlatmanın ardından **Settings** içindeki dil ayarını açıp **Türkçe** seçeneğini etkinleştirin.

Resimli adımlar için [ana sayfadaki Hızlı kurulum](https://github.com/QUINRY/snapmaker-u1-turkish-firmware#h%C4%B1zl%C4%B1-kurulum) bölümüne bakın. SHA-256 kontrolü ve güvenli kurulum ayrıntıları için [Kurulum Rehberi](https://github.com/QUINRY/snapmaker-u1-turkish-firmware/blob/main/docs/INSTALL.md) belgesini okuyun.

## Doğru paket ve taban

- Kanal: **Extended Firmware**
- Extended tabanı: `paxx12-20`
- Taban firmware: `U1_extended_1.4.1-paxx12-20_upgrade.bin`
- Taban SHA-256: `8DDB1D6DC889F8C11D6AC708DD4858439B13E830D3BF93064E857433A70FF3C3`
- UPFILE sürümü: `1.4.1.6ff6e2cf`
- Derleme tarihi alanı: `20260608141446`
- Release asset: `TURKISH_QUINRY_U1_extended_1.4.1-paxx12-20_upgrade.bin`
- Asset boyutu: `290409544` bayt
- Asset SHA-256: `3DB9844CC01A9A2EA93E02EB990EBDDE7707637CF8FB60CF3A6EAEDAFE2127D0`

Bu asset kurulum sonrasında cihazı **Extended 1.4.1-paxx12-20** tabanına geçirir; Stock 1.6.0 veya Extended 1.5.2 release asseti değildir. Resmî İngilizce Stock 1.6.0.267 üzerinden bu dosyaya geçiş aynı fiziksel U1 üzerinde başarıyla denenmiştir. Dosyayı diğer release assetlerinden tam adı, boyutu ve SHA-256 değeriyle ayırın; indirme tamamlandıktan sonra `SHA256SUMS.txt` veya `manifests/extended-1.4.1-paxx12-20.json` ile doğrulayın.

## Türkçe yerelleştirme

- Mevcut `en`, `zh`, `tw` ve `ru` dilleri değiştirilmeden beşinci dil olarak `tr-TR` / `Türkçe` eklendi.
- Yalnız Extended 1.4.1 içindeki İngilizce metinler kaynak alındı; 528 ana arayüz ve 444 hata kaydı çevrildi.
- Sürüme ait 415 bağlantı kaydı özgün değerleriyle korundu.
- Türkçe karakterler UTF-8, NFC ve BOM'suz biçimde kullanıldı.
- Ayarlar ve ilk kurulum dil seçicilerine Türkçe satırı eklendi; seçim, saklama ve yeniden yükleme yolları denetlendi.

## Doğrulama

- UPFILE checksum/MD5, RKFW başlık/son MD5 ve RKAF CRC kontrolleri geçti.
- Paket tüm katmanlarıyla temiz bir klasöre yeniden açıldı.
- Rootfs karşılaştırmasında değişen tek dosya `/usr/bin/gui` oldu.
- Dört özgün dil tablosunun baytları korundu.
- MCU bileşenleri ve rootfs dışındaki bölümler kaynak firmware ile birebir aynı kaldı.
- Son paketten GUI yeniden çıkarıldı ve beklenen Türkçe GUI SHA-256 değeriyle eşleşti.
- GUI bağımsız, davranışsal ve yeniden üretilebilirlik denetimlerinden geçti.

## Risk ve test durumu

Bu release asseti aynı fiziksel Snapmaker U1 üzerinde **resmî İngilizce Stock 1.6.0.267 üzerinden** kullanıcı tarafından yüklendi; güncelleme tamamlandı, cihaz açıldı ve Türkçe arayüz görüntülenip kullanıldı. Bu, **resmî İngilizce Stock 1.6.0.267 → Türkçe Extended 1.4.1 → Türkçe Extended 1.5.2 → Türkçe Stock 1.6.0.267** zincirinin ikinci adımıydı ve kullanıcı sorun bildirmedi. Bu kanıt tek cihazlık, kullanıcı tarafından bildirilen bir flash/boot/Türkçe arayüz smoke testidir; tam baskı döngüsünü, tüm ekranları ve donanım işlevlerini, uzun süreli kararlılığı veya kapsamlı regresyonu doğrulamaz. Firmware yükleme riski devam eder; işlem sırasında gücü kesmeyin.

## Lisans ve marka notu

Bu projenin özgün çeviri, araç ve belgeleri `GPL-3.0-only` kapsamında sunulur. Firmware içindeki Snapmaker, Extended Firmware ve diğer üçüncü taraf bileşenler kendi lisans ve telif koşullarına tabidir. Proje adları yalnız uyumluluğu ve kaynak tabanı belirtmek amacıyla kullanılmıştır.
