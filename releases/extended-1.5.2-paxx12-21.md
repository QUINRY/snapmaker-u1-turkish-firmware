# Snapmaker U1 Extended 1.5.2-paxx12-21 — Türkçe UTF-8

Bu paket, Snapmaker U1 için **Extended 1.5.2-paxx12-21** firmware'i temel alınarak hazırlanmış Türkçe UTF-8 yerelleştirmedir. Ücretsiz, kâr amacı gütmeyen ve resmî olmayan bir topluluk çalışmasıdır; Snapmaker veya Extended Firmware geliştiricileri tarafından desteklenmiş ya da onaylanmış değildir.

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
- Extended tabanı: `paxx12-21`
- Taban firmware: `U1_extended_1.5.2-paxx12-21_upgrade.bin`
- Taban SHA-256: `F85BBD0FC15FC4029ABB7EE15B5D61805AA16E47C9D4B5AA1289204D42835C0E`
- UPFILE sürümü: `1.5.2.132a88932`
- Derleme tarihi alanı: `20260722102206`
- Release asset: `TURKISH_QUINRY_U1_extended_1.5.2-paxx12-21_upgrade.bin`
- Asset boyutu: `259859532` bayt
- Asset SHA-256: `6EFE052669494B91801139C426C17E85DEE212EAF32E3F891F01AAAE7C033086`

Bu asset kurulum sonrasında cihazı **Extended 1.5.2-paxx12-21** tabanına geçirir; Stock 1.6.0 veya Extended 1.4.1 release asseti değildir. Türkçe Extended 1.4.1 üzerinden bu dosyaya geçiş aynı fiziksel U1 üzerinde başarıyla denenmiştir. Yayımlanan dosya Türkçe karakterli UTF-8 adaydır; SHA-256 değeri `946C237B...` ile başlayan eski ASCII aday bu yayına dahil edilmemiştir. Dosyayı tam adı, boyutu ve SHA-256 değeriyle ayırın; indirme tamamlandıktan sonra `SHA256SUMS.txt` veya `manifests/extended-1.5.2-paxx12-21.json` ile doğrulayın.

## Türkçe yerelleştirme

- Mevcut altı dil değiştirilmeden yedinci dil olarak `tr-TR` / `Türkçe` eklendi.
- Bu sürümün 530 ana arayüz ve 446 hata kaydı çevrildi.
- Türkçe karakterler UTF-8, NFC ve BOM'suz biçimde kullanıldı.
- Yer tutucular, satır sonları, anahtar sırası, teknik değerler ve sayısal belirteçler korundu.
- Türkçe karakter glifleri gömülü beş fontun tamamında doğrulandı; 530 arayüz metni gerçek font ölçümleriyle denetlendi.

## Doğrulama

- UPFILE başlık/bölüm checksum ve MD5 kontrolleri geçti.
- RKFW son ASCII MD5 ve RKAF CRC kontrolleri geçti.
- Paket UPFILE → RKFW → RKAF → SquashFS olarak temiz bir klasöre yeniden açıldı.
- Kaynakla semantik SquashFS karşılaştırmasında yalnız `/usr/bin/gui` farklıdır.
- MCU, boot, bootloader, U-Boot, misc, OEM, userdata, parameter ve package-file bileşenleri kaynakla birebir korundu.
- Final GUI yapısal ve davranışsal doğrulamada `59/59 PASS` aldı; seçim, kalıcı kayıt, ARM64 branch/hook/relocation ve segment izinleri denetlendi.
- Son firmware'den çıkarılan GUI, onaylanan Türkçe GUI ile byte-for-byte eşleşti.

## Risk ve test durumu

Bu release asseti aynı fiziksel Snapmaker U1 üzerinde **Türkçe Extended 1.4.1 üzerinden** kullanıcı tarafından yüklendi; güncelleme tamamlandı, cihaz açıldı ve Türkçe arayüz görüntülenip kullanıldı. Bu, **resmî İngilizce Stock 1.6.0.267 → Türkçe Extended 1.4.1 → Türkçe Extended 1.5.2 → Türkçe Stock 1.6.0.267** zincirinin üçüncü adımıydı ve kullanıcı sorun bildirmedi. Bu kanıt tek cihazlık, kullanıcı tarafından bildirilen bir flash/boot/Türkçe arayüz smoke testidir; tam baskı döngüsünü, tüm ekranları ve donanım işlevlerini, uzun süreli kararlılığı veya kapsamlı regresyonu doğrulamaz. Firmware yükleme riski devam eder; işlem sırasında gücü kesmeyin.

## Lisans ve marka notu

Bu projenin özgün çeviri, araç ve belgeleri `GPL-3.0-only` kapsamında sunulur. Firmware içindeki Snapmaker, Extended Firmware ve diğer üçüncü taraf bileşenler kendi lisans ve telif koşullarına tabidir. Proje adları yalnız uyumluluğu ve kaynak tabanı belirtmek amacıyla kullanılmıştır.
