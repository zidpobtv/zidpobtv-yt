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
