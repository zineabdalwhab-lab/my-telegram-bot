import telebot
import os

# ضع هنا التوكن الخاص بك بدلاً من هذه الجملة
API_TOKEN = '8756704689:AAFEIEkwll_4e9_uHecsyGsop4ZVunDzm0o'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! أنا بوت عبد الوهاب الجديد.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "لقد استلمت رسالتك!")

bot.infinity_polling()
