

import telebot
import os
from flask import Flask
from threading import Thread

# التوكن الصحيح الخاص بك
BOT_TOKEN = "8892512718:AAH73fJFBNOZJRSYGGhQ4O3-pNx3Aiie5lc"
bot = telebot.TeleBot(BOT_TOKEN)

# سيرفر وهمي لإبقاء منصة Render مستقرة وتعمل مجاناً
app = Flask('')

@app.route('/')
def home():
    return "Bot is running online 24/7!"

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

# تشغيل السيرفر في خلفية منفصلة
Thread(target=run).start()

# أوامر البوت
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! أرسل لي رابط إنستغرام وسأقوم بتحميله فوراً 🚀")

# تشغيل البوت الأساسي باستمرار
print("البوت انطلق ويعمل الآن سحابياً...")
bot.infinity_polling()

