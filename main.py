import telebot
import time
import threading

API_TOKEN = '8756704689:AAFEIEkwl1_4e9_uHecsyGsop4ZVunDzm0o'
bot = telebot.TeleBot(API_TOKEN)

# متغير لتتبع الجلسات
sessions_done = 0

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك يا عبد الوهاب! استخدم أمر /pomodoro للبدء بجلسة دراسة.")

@bot.message_handler(commands=['pomodoro'])
def start_pomodoro(message):
    global sessions_done
    if sessions_done < 12:
        sessions_done += 1
        bot.reply_to(message, f"بدأت الجلسة رقم {sessions_done} من 12. التركيز لمدة 90 دقيقة!")
        
        # ننتظر 90 دقيقة (ساعة ونصف)
        time.sleep(90 * 60) 
        
        bot.reply_to(message, "انتهت الجلسة! خذ استراحة لمدة 10 دقائق ثم عد للعمل.")
    else:
        bot.reply_to(message, "لقد أتممت 12 جلسة اليوم! أحسنت، حان وقت النوم الآن.")

bot.infinity_polling()
