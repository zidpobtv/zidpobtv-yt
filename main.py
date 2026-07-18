from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Zidpob TV Bot Aktif!"

def run():
    app.run(host='0.0.0.0', port=8080)

t = Thread(target=run)
t.start()

# Buradan sonra senin video oluşturma ve hikaye yazma kodların gelecek


import time

# --- YUKARIDAKİ FLASK KODLARI BURADA KALACAK ---

# Botun ana döngüsü
def ana_döngü():
    while True:
        print("Zidpob TV: Yeni hikaye kontrol ediliyor...")
        
        # --- BURAYA SENİN HİKAYE ÜRETME VE VİDEO RENDER KOMUTLARINI EKLEYECEKSİN ---
        # Örnek: generate_story()
        # Örnek: render_video()
        
        print("Zidpob TV: İşlem tamamlandı, 1 saat bekleniyor.")
        time.sleep(3600)  # 3600 saniye = 1 saat bekler

# Döngüyü arka planda başlat
if __name__ == "__main__":
    # Ana döngüyü ayrı bir iş parçacığında çalıştırıyoruz ki Flask kapanmasın
    döngü_thread = Thread(target=ana_döngü)
    döngü_thread.start()
        
