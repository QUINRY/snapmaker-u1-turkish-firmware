# Snapmaker U1 Extended 1.4.1 Türkçe Firmware Raporu

## Çıktı

- Kaynak: `U1_extended_1.4.1-paxx12-20_upgrade.bin`
- Türkçe firmware: `U1_extended_1.4.1-paxx12-20_TR_upgrade.bin`
- Firmware sürümü: `1.4.1.6ff6e2cf`
- Derleme tarihi alanı: `20260608141446`
- Çıktı boyutu: `290409544` bayt
- Çıktı SHA-256: `3DB9844CC01A9A2EA93E02EB990EBDDE7707637CF8FB60CF3A6EAEDAFE2127D0`

Kaynak firmware değiştirilmedi. Kaynak dosyanın yeniden doğrulanan SHA-256 değeri:

`8DDB1D6DC889F8C11D6AC708DD4858439B13E830D3BF93064E857433A70FF3C3`

## Dil yapısı

- Yalnızca bu 1.4.1 Extended firmware içindeki İngilizce metinler kaynak alındı.
- Mevcut `en`, `zh`, `tw` ve `ru` dilleri korunarak beşinci dil olarak `tr-TR` eklendi.
- Türkçe karakterler UTF-8 olarak kullanıldı: `ç, ğ, ı, ö, ş, ü, Ç, Ğ, İ, Ö, Ş, Ü`.
- Ana arayüz tablosundaki 528, hata tablosundaki 444 kayıt çevrildi.
- 415 bağlantı kaydı sürüme ait özgün değerleriyle korundu.
- Türkçe JSON dosyaları UTF-8 (BOM'suz), NFC, anahtar sırası, yer tutucular, teknik değerler ve satır sonları bakımından doğrulandı.
- Ayarlar ve ilk kurulum dil seçicilerine `Türkçe` satırı eklendi; seçim, saklama ve yeniden yükleme yolları denetlendi.

## Paket doğrulaması

- GUI yaması bağımsız ve yeniden üretilebilir doğrulamalardan geçti.
- Dört özgün dil tablosunun baytları korundu.
- Rootfs karşılaştırmasında değişen tek dosya `/usr/bin/gui` oldu.
- Son rootfs boyutu: `251027456` bayt.
- Rootfs bölümünde kalan alan: `63545344` bayt (yaklaşık 60.60 MiB).
- RKAF CRC, RKFW başlık/MD5 ve dış UPFILE bölüm sağlama toplamları başarıyla doğrulandı.
- MCU bileşenleri ve rootfs dışındaki bölümler kaynak firmware ile birebir aynı kaldı.
- Son paketten GUI yeniden çıkarıldı ve beklenen Türkçe GUI SHA-256 değeriyle eşleşti.

## Önemli not

Paket biçimi ve iç bütünlük kontrolleri tamamlandı; ancak fiziksel bir Snapmaker U1 üzerinde flash, açılış ve ekran testi yapılmadı. Firmware yükleme işlemi her özel firmware kullanımında olduğu gibi kullanıcı sorumluluğundadır.
