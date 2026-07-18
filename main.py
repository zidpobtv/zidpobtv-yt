from flask import Flask
from threading import Thread
import time

app = Flask('')

@app.route('/')
def home():
    return "Zidpob TV Bot Aktif!"

def run():
    app.run(host='0.0.0.0', port=8080)

# Botun ana döngüsü
def ana_döngü():
    while True:
        print("Zidpob TV: Yeni hikaye kontrol ediliyor...")
        # BURAYA OTOMASYON KODLARINI (story.py çağrılarını) EKLEYECEKSİN
        print("Zidpob TV: İşlem tamamlandı, 1 saat bekleniyor.")
        time.sleep(3600)  # 1 saat bekler

if __name__ == "__main__":
    # Flask sunucusunu ayrı bir thread'de başlat
    server = Thread(target=run)
    server.start()
    
    # Ana döngüyü başlat
    ana_döngü()
    
