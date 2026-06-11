import telebot
import g4f

bot = telebot.TeleBot("8939044527:AAEiWhP7-B5mHlU4mC3-0uLB3_-8D3X3BpQ")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Men Jamilov Kamol tomonidan yaratilgan sun'iy intellektman. Qanaqa savollaringiz bor?")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_35_turbo,
            messages=[{"role": "user", "content": message.text}],
        )
        bot.reply_to(message, response)
    except Exception as e:
        bot.reply_to(message, "Kechirasiz, hozir savolingizga javob bera olmayapman.")

bot.infinity_polling()
