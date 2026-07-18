from flask import Flask
from threading import Thread
import time
import os
from google import genai # Yeni kütüphane

# API anahtarını tanımla
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

app = Flask('')

@app.route('/')
def home():
    return "Zidpob TV Bot Aktif!"

def run():
    app.run(host='0.0.0.0', port=8080)

def hikaye_uret():
    # Yeni kütüphanede model kullanımı
    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents="Toby adında bir karakter için, çocuklar için eğitici ve eğlenceli, kısa bir macera hikayesi yaz."
    )
    return response.text

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
        time.sleep(3600)

if __name__ == "__main__":
    server = Thread(target=run)
    server.start()
    ana_döngü()
    
