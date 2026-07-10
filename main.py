import telebot
import os

API_TOKEN = '8756704689:AAFEIEkwl1_4e9_uHecsyGsop4ZVunDzm0o'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! البوت عاد للعمل.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "استلمت رسالتك!")

bot.infinity_polling()
