#pip install pyTelegramBotAPI
import os
import inter

import telebot

BOT_TOKEN="6161492376:AAHtd7EhzL8uiS9iOjdFdQUXLzvJ4p0_icM"

bot = telebot.TeleBot(BOT_TOKEN)
    
@bot.message_handler(commands=['login'])
def send_welcome(message):
    print("login")
    bot.reply_to(message, "login successful")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    print(message.text)
    # bot.reply_to(message, message.text)
    response = inter.resp(message.text)
    bot.reply_to(message, response)

bot.infinity_polling()