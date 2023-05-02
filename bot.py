#pip install pyTelegramBotAPI
import os
import chat

import telebot

BOT_TOKEN="6222189484:AAHlzKGBiNOCt6aW3-dKJtHchC7dTAtfQB8"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    print("start")
    bot.reply_to(message, "Welcome to te nimble task manager!")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    print(message.text)
    # bot.reply_to(message, message.text)
    response = chat.resp(message.text)
    bot.reply_to(message, response)

bot.infinity_polling()


