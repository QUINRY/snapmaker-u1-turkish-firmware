# Snapmaker U1 Extended 2.0.0-paxx12-develop-7188aab — Türkçe

Snapmaker U1'in **2.0.0 rolling/develop** sürümüne, hem Snapmaker hem de isteğe bağlı **HelixScreen 1.0.0** arayüzünde Türkçe desteği ekler. Mevcut diller korunur. Ücretsiz ve kâr amacı gütmeyen, resmî olmayan bir topluluk çalışmasıdır.

> **Kaynak / Credits:** [paxx12-snapmaker-u1/SnapmakerU1-Extended-Firmware](https://github.com/paxx12-snapmaker-u1/SnapmakerU1-Extended-Firmware/releases/tag/rolling) projesine ve katkıda bulunanlara teşekkürler. Bu paket standart Extended çeşidinin **7188aab** derlemesine dayanır. Kaynak rolling yayını güncellenebilir; buradaki Türkçe dosya belirtilen derlemeye sabitlenmiştir ve **Pre-release** olarak yayımlanır.

> **HelixScreen / Credits:** [prestonbrown/helixscreen v1.0.0](https://github.com/prestonbrown/helixscreen/releases/tag/v1.0.0). HelixScreen'in özgün geliştirmesi bu projenin geliştiricilerine aittir.

## Hızlı kurulum

1. **Assets** bölümünden `TURKISH_QUINRY_U1_extended_2.0.0-paxx12-develop-7188aab_upgrade.bin` dosyasını indirin ve aşağıdaki SHA-256 değeriyle doğrulayın.
2. `.bin` dosyasını **FAT32** USB belleğe kopyalayıp belleği yazıcıya takın.
3. **Settings → About → Firmware Version → Local Update** yolundan dosyayı seçip onaylayın.
4. Güncelleme tamamlanıp yazıcı açılana kadar gücü kesmeyin ve belleği çıkarmayın.
5. Dil ayarlarından **Türkçe** seçin.

Menü adları kurulum öncesindeki İngilizce biçimiyle verilmiştir. [Resimli kurulum](https://github.com/QUINRY/snapmaker-u1-turkish-firmware#h%C4%B1zl%C4%B1-kurulum) · [Dosya doğrulama](https://github.com/QUINRY/snapmaker-u1-turkish-firmware/blob/main/docs/VERIFY.md)

## Dosya bilgileri

- Dosya: `TURKISH_QUINRY_U1_extended_2.0.0-paxx12-develop-7188aab_upgrade.bin`
- Boyut: `256600836` bayt
- SHA-256: `33639F5149894F44835206223DDAAED02E8BB4320170C98FE781C2F9F96AAA57`
- Kaynak: `U1_extended_2.0.0-paxx12-develop-7188aab_upgrade.bin`
- Kaynak SHA-256: `FCFDD99CA6D6B4C3B7566BDA625A2C24FF8F7C359A073F151E3E073080647976`
- Kaynak commit: [`7188aab`](https://github.com/paxx12-snapmaker-u1/SnapmakerU1-Extended-Firmware/commit/7188aab2fc8c671bc467925a0ad8cdea6d8668f1)
- Korunan UPFILE sürümü/tarihi: `2.0.0.2047188aab` / `20260907182340`

## Türkçe içerik

- 550 arayüz metni ve 466 hata kaydı; Türkçe karakterli UTF-8/NFC.
- Bu firmware'den çıkarılan İngilizce kaynaklarda **27 yeni veya değişmiş metin** yeniden çevrildi. Diğer 989 karşılık yalnız anahtar ve İngilizce metin birebir eşleştiğinde kullanıldı.
- Yeni motor titreşim telafisi, 0.2 mm nozül uyumluluğu ve oturum kapatma açıklamaları çevrildi.
- Fransızca dahil yedi mevcut dil korundu. Türkçe, yeni dil kaydı ve menü düzenine sekizinci seçenek olarak eklendi.
- İsteğe bağlı **HelixScreen 1.0.0** için ayrıca **2.868 metin** çevrildi. 23 yeni metin güncel İngilizce kaynaktan çevrildi; 2.845 karşılık yalnız birebir kaynak eşleşmesiyle kullanıldı. Dokuz mevcut dil korunarak Türkçe onuncu seçenek olarak eklendi.

## HelixScreen kullanımı

HelixScreen zorunlu değildir; varsayılan Snapmaker arayüzü korunur. Extended ayarlarında **Touchscreen GUI (Experimental) → HelixScreen** seçildiğinde orijinal paket indirilir ve doğrulanan Türkçe dosyalar otomatik uygulanır. Ardından HelixScreen'in dil ayarından **Türkçe** seçin. Önceden kurulu, bu sürümle birebir eşleşen HelixScreen 1.0.0 da açılışta desteklenir.

Dil tercihiniz ve diğer ayarlarınız otomatik değiştirilmez. Farklı veya özelleştirilmiş HelixScreen dosyaları üzerine yazılmaz. HelixScreen'i ileride başka bir sürüme güncellerseniz o sürüm için ayrıca hazırlanmış Türkçe paket gerekebilir.

## Doğrulama ve test durumu

Final firmware tüm katmanlarıyla yeniden açıldı. Paket checksum/MD5/CRC kontrolleri geçti. Yalnız onaylanan Türkçe arayüz dosyaları, HelixScreen kurulum bağlantıları ve çeviri kaynakları değişti/eklendi; diğer dosyalar, izinler ve rootfs dışındaki bölümler korundu. Final Snapmaker GUI **85/85 PASS**, HelixScreen dil yaması **41/41 PASS** aldı. Dil seçim/kayıt yolları kontrollü emülasyonla sınandı; bu fiziksel ekran testi değildir. HelixScreen kurucusu, orijinal 1.0.0 paketinin yalıtılmış kopyasında çalıştırılıp dosyalar karşılaştırıldı; ayarlar ve diğer diller korundu.

Bu 2.0.0 Türkçe paketinin fiziksel yazıcıda yükleme/açılış testi henüz bildirilmedi. Ana sürüm isteyenler [Extended 1.6.0 Türkçe](https://github.com/QUINRY/snapmaker-u1-turkish-firmware/releases/tag/u1-extended-1.6.0-paxx12-22-tr-r1) paketini kullanabilir.

## Lisans

Özgün çeviri, araç ve belgeler `GPL-3.0-only` kapsamındadır. Snapmaker ve Extended Firmware bileşenleri kendi lisans koşullarına tabidir. Türkçe çalışma bu projeler tarafından onaylanmış veya desteklenmiş değildir.
