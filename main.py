from flask import Flask
from threading import Thread
import time
import os
import google.generativeai as genai

# Gemini API yapılandırması
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
# Model ismini tamamen kaldırıp varsayılanı kullanmayı dene
model = genai.GenerativeModel()

app = Flask('')

@app.route('/')
def home():
    return "Zidpob TV Bot Aktif!"

def run():
    app.run(host='0.0.0.0', port=8080)

# Gemini'den hikaye alma fonksiyonu
def hikaye_uret():
    prompt = "Toby adında bir karakter için, çocuklar için eğitici ve eğlenceli, kısa bir macera hikayesi yaz."
    response = model.generate_content(prompt)
    return response.text

# Botun ana döngüsü
def ana_döngü():
    while True:
        print("Zidpob TV: Gemini'den hikaye isteniyor...")
        try:
            hikaye = hikaye_uret()
            print("--- ÜRETİLEN HİKAYE BAŞLANGICI ---")
            print(hikaye)
            print("--- ÜRETİLEN HİKAYE SONU ---")
        except Exception as e:
            print(f"Hata oluştu: {e}")
        
        print("Zidpob TV: İşlem tamamlandı, 1 saat bekleniyor.")
        time.sleep(3600)  # 3600 saniye = 1 saat

if __name__ == "__main__":
    # Flask sunucusunu ayrı bir thread'de başlat
    server = Thread(target=run)
    server.start()
    
    # Ana döngüyü başlat
    ana_döngü()
    
