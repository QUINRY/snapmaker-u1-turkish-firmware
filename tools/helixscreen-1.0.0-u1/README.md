# HelixScreen 1.0.0 U1 Türkçe kaynakları

Bu araçlar, HelixScreen'in **Snapmaker U1 için v1.0.0** paketine onuncu dil olarak Türkçe eklenen dosyaları yeniden üretir. Mevcut dokuz dil ve kullanıcı ayarları korunur. Türkçe ilk kurulum seçeneği metin olarak gösterilir; mevcut bayraklar değişmez.

## Kaynak paket

[HelixScreen v1.0.0 yayını](https://github.com/prestonbrown/helixscreen/releases/tag/v1.0.0) içindeki [Snapmaker U1 arşivini](https://github.com/prestonbrown/helixscreen/releases/download/v1.0.0/helixscreen-snapmaker-u1-v1.0.0.tar.gz) indirin. Başka bir platformun veya sürümün paketini kullanmayın.

Arşiv SHA-256:

```text
49c9aae95c1be859ea6d75691f55dc8d69cc0bd679da6cf1d58d9ca14a82844a
```

Arşivi `build/helix-official` klasörüne açın; bu klasörün altında `helixscreen/bin/helix-screen` bulunmalı. Aşağıdaki komutlar depo kökünden, Python 3.12 ortamında çalıştırılır.

## Dil kaynakları ve kurulum sihirbazı

`rebuild_resources.py` yalnızca Python standart kitaplığını kullanır. Güncel İngilizce kaynakları, kaynak dosya hash'lerini, 2.868 anahtarı, yer tutucuları ve mevcut dil değerlerini doğrular. Eski HelixScreen çalışma klasörüne ihtiyaç duymaz.

```sh
python tools/helixscreen-1.0.0-u1/rebuild_resources.py --official-root build/helix-official/helixscreen --translation translations/helixscreen/1.0.0-snapmaker-u1/tr.xml --output build/helix-tr
```

Çıktılar `ui_xml/translations/tr.xml`, `ui_xml/translations/translations.xml`, `ui_xml/wizard_language_chooser.xml` ve `resource_rebuild_report.json` dosyalarıdır. Girdi klasörüne yazılmaz. Aynı çıktıyla yeniden çalıştırılabilir; farklı içerikte mevcut çıktı dosyalarının üzerine yazılmaz.

XML çıktısının satır sonları sabittir; Git'in girdi dosyasında LF/CRLF dönüşümü yapması çıktı hash'lerini değiştirmez.

Yayımlanan Türkçe dosyasıyla beklenen SHA-256 değerleri:

| Dosya | SHA-256 |
| --- | --- |
| `tr.xml` | `e7594151ea7f710474f13797b0b03eaf3bc62b4219beeee3ff832ab81849843d` |
| `translations.xml` | `07c39784d7c1b7dd73ee4d9705b20462436d0be5b7f3f083ea6d5724aef0f108` |
| `wizard_language_chooser.xml` | `9780f119603e324d6d781562ab114da7d314734fc78992f8e9635c924f8efecd` |

## Ekran uygulaması

Türkçenin ayarlar ve ilk kurulum dil listesinde görünmesi için sürüme özel uygulama yaması da gereklidir. Python 3.12 ortamına bağımlılıkları yükleyin:

```sh
python -m pip install pyelftools keystone-engine capstone angr
python tools/helixscreen-1.0.0-u1/patch_helix_u1_tr.py --source build/helix-official/helixscreen/bin/helix-screen --output build/helix-tr/bin/helix-screen --patch-manifest build/helix-tr/patch_manifest.json --verification-report build/helix-tr/verification_report.json
python tools/helixscreen-1.0.0-u1/patch_helix_u1_tr.py --verify --source build/helix-official/helixscreen/bin/helix-screen --output build/helix-tr/bin/helix-screen --patch-manifest build/helix-tr/patch_manifest.json --verification-report build/helix-tr/fresh_verification_report.json
```

Uygulama yaması kaynak ELF dosyasının SHA-256 değerine kilitlidir. Mevcut dil kayıtlarını korur; Türkçe dil kodunu, ayarlar seçeneğini ve ilk kurulum indeksini ekler. Statik ELF denetimleri ve AArch64 kod parçalarının emülasyonu; dil eşlemeleri, seçenekler, karşılama döngüsü ve geçersiz indeks davranışını kontrol eder. Haricî arayüz ve sistem çağrılarının bir kısmı test içinde temsil edilir. Bu kontroller gerçek ekran görüntüsü, dokunmatik giriş veya fiziksel yazıcı testi değildir.

Burada üretilen dosyalar HelixScreen yüküdür; tek başına flashlanabilir firmware oluşturmaz. Firmware içindeki `helixscreen-turkish-install` betiği yalnızca eşleşen U1 1.0.0 kurulumuna uygulanır ve kullanıcı ayarlarını değiştirmez. Üst projenin kaynakları ve lisansları [HelixScreen deposundadır](https://github.com/prestonbrown/helixscreen/tree/v1.0.0).
