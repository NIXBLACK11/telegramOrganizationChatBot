#pip install pyTelegramBotAPI
import os
import telebot
from dotenv import load_dotenv

# Load variables from .env into the environment
load_dotenv()

BOT_TOKEN = "6663036335:AAFYeRj99HAC6B8rD1cab04F_WpUr6pwxXE"

bot = telebot.TeleBot(BOT_TOKEN)
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    response = "To login type /login and Enter the login and password\nexamlpe:\ntest test@123\nTo check pubic details just ask ex:What are the interest rates"
    bot.reply_to(message, response)    

@bot.message_handler(commands=['login'])
def send_welcome(message):
    global l
    response = "Enter the login and password\nexamlpe:\ntest test@123"
    l = True
    bot.reply_to(message, response)

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    print(message.text)
    
    # bot.send_photo(chat_id, photo=open('monthly_expenditures.png', 'rb'))
    bot.reply_to(message, response)

bot.infinity_polling()