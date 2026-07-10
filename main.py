from telethon import TelegramClient, events
import os

# ضع بياناتك التي استخرجناها من my.telegram.org
API_ID = '30653012'
API_HASH = '988bc3a735d603cc4388a776777a66d4'
BOT_TOKEN = '8756704689:AAFEIEkwl1_4e9_uHecsyGsop4ZVunDzm0o'

# إنشاء العميل الخاص بالبوت
client = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('أنا الآن أعمل بمكتبة Telethon وجاهز لمراقبة البث!')

print("البوت يعمل الآن...")
client.run_until_disconnected()
