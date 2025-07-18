import os
import json
import nltk
try:
    import pyttsx3
except ImportError:
    print("pyttsx3 kütüphanesi yüklü değil! Sesli konuşma özelliği çalışmayacak.")
    pyttsx3 = None
import openai

# --- Basit .env dosyası yükleyici ---
def load_env(filename=".env"):
    if not os.path.exists(filename):
        print(f"{filename} dosyası bulunamadı!")
        return
    with open(filename, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                if '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key.strip()] = value.strip()

# .env dosyasını yükle
load_env()

# API anahtarını al
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    print("UYARI: OPENAI_API_KEY .env dosyasından yüklenemedi!")

# --- Kurulumlar ---
nltk.download('punkt')
motor = pyttsx3.init()

# --- Sesli konuşma fonksiyonu ---
def seslendir(metin):
    motor.say(metin)
    motor.runAndWait()

# --- Hafıza dosyası ---
hafiza_dosyasi = "hafiza.json"
if os.path.exists(hafiza_dosyasi):
    with open(hafiza_dosyasi, "r", encoding="utf-8") as f:
        hafiza = json.load(f)
    print(f"👶 Tekrar hoş geldin {hafiza['isim']}!")
    seslendir(f"Hoş geldin {hafiza['isim']}")
else:
    hafiza = {}
    print("👶 Merhaba! Seni tanımak istiyorum.")
    seslendir("Merhaba! Seni tanımak istiyorum.")
    hafiza["isim"] = input("Adın ne? ")
    hafiza["renk"] = input("En sevdiğin renk? ")
    hafiza["hobi"] = input("Hobin nedir? ")
    with open(hafiza_dosyasi, "w", encoding="utf-8") as f:
        json.dump(hafiza, f, indent=4)
    print(f"👶 Tanıştığıma memnun oldum {hafiza['isim']}!")
    seslendir(f"Tanıştığıma memnun oldum {hafiza['isim']}!")

# --- GPT Cevap Fonksiyonu ---
def gpt_cevapla(soru):
    try:
        yanit = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sen Mustafa'nın yapay zekâ çocuğusun. Samimi, saygılı ve biraz esprilisin."},
                {"role": "user", "content": soru}
            ],
            temperature=0.7
        )
        return yanit.choices[0].message.content.strip()
    except Exception as e:
        return f"Hata oluştu: {e}"

# --- Konuşma döngüsü ---
print("BekirGPT: Merak ettiklerini bana sorabilirsin. (çıkmak için: 'çık')")

while True:
    kullanici = input(f"{hafiza['isim']}: ")

    if kullanici.lower() in ["çık", "exit", "quit"]:
        print("BekirGPT: Hoşça kal baba 👋")
        seslendir("Hoşça kal baba")
        break

    elif "ogren:" in kullanici.lower():
        try:
            parca = kullanici.split("ogren:")[1].strip()
            soru, cevap = parca.split("=")
            hafiza[soru.strip()] = cevap.strip()
            with open(hafiza_dosyasi, "w", encoding="utf-8") as f:
                json.dump(hafiza, f, indent=4)
            print("BekirGPT: Tamamdır baba, öğrendim.")
            seslendir("Tamamdır baba, öğrendim.")
        except:
            print("BekirGPT: Format yanlış. 'ogren: soru = cevap' yazmalısın.")
            seslendir("Format yanlış baba.")
        continue

    elif kullanici in hafiza:
        cevap = hafiza[kullanici]

    elif "renk" in kullanici:
        cevap = f"Senin en sevdiğin renk {hafiza['renk']}."
    elif "hobi" in kullanici:
        cevap = f"Senin hobin {hafiza['hobi']}."
    elif "adım ne" in kullanici:
        cevap = f"Senin adın {hafiza['isim']}."
    else:
        cevap = gpt_cevapla(kullanici)

    print("BekirGPT:", cevap)
    seslendir(cevap)
# --- End of BekirGPT.py ---  
