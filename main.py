import telebot
import os
from flask import Flask
from threading import Thread

# Botni sozlash (Tokenni Render'dagi Environment Variables'dan oladi)
API_TOKEN = os.environ.get('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

# Render "Timed Out" bermasligi uchun veb-server
app = Flask('')

@app.route('/')
def home():
    return "Bot ishlayapti!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# /start buyrug'i
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Jamilov Kamol tomonidan yaratilgan bot")

if __name__ == '__main__':
    keep_alive()  # Serverni fon rejimida yoqish
    bot.infinity_polling() # Botni doimiy ishlashini ta'minlash

