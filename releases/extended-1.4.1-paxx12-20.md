# Snapmaker U1 Extended 1.4.1-paxx12-20 — Türkçe

Bu paket, Snapmaker U1 için **Extended 1.4.1-paxx12-20** firmware'i temel alınarak hazırlanmış Türkçe yerelleştirmedir. Ücretsiz, kâr amacı gütmeyen ve resmî olmayan bir topluluk çalışmasıdır; Snapmaker veya Extended Firmware geliştiricileri tarafından desteklenmiş ya da onaylanmış değildir.

## Hızlı kurulum

> Türkçe firmware henüz kurulmadığı için menü adları yazıcıda göründüğü İngilizce biçimiyle verilmiştir.

1. Bu release'teki `.bin` dosyasını indirin.
2. Dosyayı **FAT32** biçimli USB belleğin kök dizinine kopyalayın ve belleği yazıcıya takın.
3. Dokunmatik ekranda **Settings → About** bölümünü açıp **Version** satırına dokunun.
4. Sağ üstteki **Local Update** seçeneğine girin.
5. USB bellekteki `.bin` dosyasını seçip güncellemeyi onaylayın.
6. Güncelleme tamamlanıp yazıcı yeniden başlayana kadar gücü kesmeyin ve USB belleği çıkarmayın.
7. Yeniden başlatmanın ardından **Settings** içindeki dil ayarını açıp **Türkçe** seçeneğini etkinleştirin.

SHA-256 kontrolü ve güvenli kurulum ayrıntıları için [Kurulum Rehberi](https://github.com/QUINRY/snapmaker-u1-turkish-firmware/blob/main/docs/INSTALL.md) belgesini okuyun.

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

Bu asset yalnız **Extended 1.4.1-paxx12-20** tabanı içindir; Stock 1.6.0 veya Extended 1.5.2 paketi değildir. İndirme tamamlandıktan sonra dosya özetini `SHA256SUMS.txt` veya `manifests/extended-1.4.1-paxx12-20.json` ile doğrulayın.

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

Bu yayın için rapora kaydedilmiş fiziksel Snapmaker U1 flash, açılış veya gerçek ekran yerleşim testi **yoktur**. Paket statik, emüle edilmiş ve katman katman bütünlük kontrollerinden geçmiştir; bu kontroller fiziksel cihaz testinin yerini tutmaz. Firmware yükleme işlemi başarısız olursa cihaz kurtarma işlemi gerekebilir. Yükleme kararı ve sonuçları kullanıcı sorumluluğundadır; işlem sırasında güç kesilmemesini sağlayın.

## Lisans ve marka notu

Bu projenin özgün çeviri, araç ve belgeleri `GPL-3.0-only` kapsamında sunulur. Firmware içindeki Snapmaker, Extended Firmware ve diğer üçüncü taraf bileşenler kendi lisans ve telif koşullarına tabidir. Proje adları yalnız uyumluluğu ve kaynak tabanı belirtmek amacıyla kullanılmıştır.
