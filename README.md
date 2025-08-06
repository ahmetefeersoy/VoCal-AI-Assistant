# VoCal-AI-Assistant

VoCal, müşterilerin sesli komutlarla kolayca randevu almasını sağlayan yapay zekâ destekli bir sanal asistandır. Google Takvim entegrasyonu ile randevuları otomatik olarak kaydeder. Farklı sektörlerdeki işletmelere kolayca uyarlanabilecek şekilde tasarlanmıştır.

---

## 🚀 Özellikler

- 🎙️ **Sesli İletişim:** Web tabanlı mikrofon erişimi ile sesli komutları alır.  
- 📅 **Google Takvim Entegrasyonu:** Randevuları otomatik olarak Google Takvim’e kaydeder.  
- 🧠 **Gemini Modeli ile NLP:** Metin tabanlı randevu isteklerini anlamak için Gemini kullanılır.  
- ⚙️ **JSON Tabanlı Dinamik Yapılandırma:** İşletme bilgileri ve ayarları yapılandırma dosyalarıyla yönetilir.  
- 🏥 **Sektör Bağımsız:** Dişçi, berber, veteriner gibi farklı işletmelere kolayca entegre edilebilir.

---

## 🧱 Teknolojiler

- Python
- WebRTC veya benzeri teknolojilerle web tabanlı sesli iletişim  
- Gemini NLP modeli (Google Bard API vb.)  
- Google Calendar API  
- JSON yapılandırma dosyaları

---

## 🗂️ Proje Yapısı

VoCal/
├── Configs/ # İşletme bazlı ayarlar (örneğin berber.json)
├── app/ # STT, TTS, NLP ve Takvim servisleri
├── README.md


---

## 🔁 Entegrasyon Kolaylığı

Yeni bir işletme eklemek için sadece `Configs/` klasörüne yeni bir yapılandırma dosyası eklemeniz yeterlidir.

Örnek yapılandırma dosyaları:  
- `Configs/berber.json`  
- `Configs/disci.json`  
- `Configs/veteriner.json`

Her yapılandırma dosyasında şu bilgiler bulunur:  
- Patron adı  
- Lokasyon  
- Meslek  
- Çalışma saatleri  
- Tatil günleri  
- Sunulan hizmetler  
- Google Calendar bağlantısı  
- Sesli yanıt şablonları

---

## ✨ Kullanım Senaryosu

- **Müşteri:** “Merhaba, yarın saat 4’te saç kestirmek istiyorum.”  
- **VoCal:** “Tamamdır, randevunuzu yarın saat 16:00’ya ayarladım.”

---

## 📌 Geliştirme Aşamaları

1. 🎙️ Web tarayıcı üzerinden mikrofonla müşteri sesini alma (Speech-to-Text)  
2. 📄 Gemini modeli ile metni analiz ederek randevu niyetini anlama  
3. 📆 Google Calendar’a randevu ekleme  
4. 🔊 Text-to-Speech ile randevu sonucunu sesli olarak kullanıcıya geri bildirme
