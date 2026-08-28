# Snapmaker U1 Extended 1.5.2-paxx12-21 — Türkçe UTF-8

Bu paket, Snapmaker U1 için **Extended 1.5.2-paxx12-21** firmware'i temel alınarak hazırlanmış Türkçe UTF-8 yerelleştirmedir. Ücretsiz, kâr amacı gütmeyen ve resmî olmayan bir topluluk çalışmasıdır; Snapmaker veya Extended Firmware geliştiricileri tarafından desteklenmiş ya da onaylanmış değildir.

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

Bu asset yalnız **Extended 1.5.2-paxx12-21** tabanı içindir; Stock 1.6.0 veya Extended 1.4.1 paketi değildir. Yayımlanan dosya Türkçe karakterli UTF-8 adaydır. SHA-256 değeri `946C237B...` ile başlayan eski ASCII aday bu yayına dahil edilmemiştir. İndirme tamamlandıktan sonra dosya özetini `SHA256SUMS.txt` veya `manifests/extended-1.5.2-paxx12-21.json` ile doğrulayın.

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

Bu yayın için rapora kaydedilmiş fiziksel Snapmaker U1 flash, açılış veya gerçek ekran yerleşim testi **yoktur**. Paket statik, emüle edilmiş ve katman katman bütünlük kontrollerinden geçmiştir; bu kontroller fiziksel cihaz testinin yerini tutmaz. Firmware yükleme işlemi başarısız olursa cihaz kurtarma işlemi gerekebilir. Yükleme kararı ve sonuçları kullanıcı sorumluluğundadır; işlem sırasında güç kesilmemesini sağlayın.

## Lisans ve marka notu

Bu projenin özgün çeviri, araç ve belgeleri `GPL-3.0-only` kapsamında sunulur. Firmware içindeki Snapmaker, Extended Firmware ve diğer üçüncü taraf bileşenler kendi lisans ve telif koşullarına tabidir. Proje adları yalnız uyumluluğu ve kaynak tabanı belirtmek amacıyla kullanılmıştır.
