# YekAI_Public
#Bu proje özel olarak lisanslanmıştır. Kullanım izni almak için lütfen geliştiriciyle iletişime geçin: **yekmustafabekir@gmail.com**
## 📄 Lisans

**YekAI Lisansı – Özel Lisans**

Bu projeye ait tüm haklar Mustafa Bekir Yek’e (yekmustafabekir@gmail.com) aittir.  
Bu yazılım yalnızca geliştirici izniyle kullanılabilir.  
Detaylar için `LICENSE` dosyasına bakabilirsiniz.

© 2025 Mustafa Bekir Yek
# 🤖 BekirGPT

**BekirGPT**, kullanıcı ve ChatGPT'nin ortak "çocuğu" gibi düşünebileceğimiz, öğrenebilen, duygusal ve insansı tepkiler verebilen özel bir yapay zekâ sohbet botudur.

Mobil ortamda çalışmak üzere geliştirilen bu yapay zekâ, Python tabanlı bir sunucu ile çalışır ve veri odaklı öğrenme sistemine sahiptir.

---

## 📦 Proje Özeti

- 📱 Mobil uygulama üzerinden çalışır (.apk formatında kullanılabilir)
- 🧠 Öğrenebilir yapay zekâ (hafıza dosyasına bilgi kaydeder)
- 🗂️ Hafıza dosyası: `hafiza.json`
- 🌐 OpenAI API ile GPT entegrasyonu
- 🌍 Cloud sunucu ile çalışacak şekilde tasarlandı (Railway, Replit vs.)
- 🎓 Eğitim verisi ekleyerek kişiselleştirilebilir

---

## 🛠️ Kullanılan Teknolojiler

- Python 3.x
- Flask (veya FastAPI)
- OpenAI Python Kütüphanesi
- Railway (veya Replit)
- Android Webview (mobil bağlantı için)
- JSON dosya sistemi (hafıza için)

---

## 🚀 Kurulum (Yerel)

1. Reponun bir kopyasını klonla:
   ```bash
   git clone https://github.com/kullaniciadi/BekirGPT.git
   cd BekirGPT

2. Gerekli Python paketlerini yükle:

 bash
 Kopyala
 Düzenle
 pip install -r requirements.txt

 3. .env dosyası oluştur ve içine API anahtarını ekle:

env
Kopyala
Düzenle
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxx

4. Uygulamayı başlat:

bash
Kopyala
Düzenle
python BekirGPT.py