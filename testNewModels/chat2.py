import logging
from telegram.ext import Updater, CommandHandler, CallbackContext

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Set your Telegram bot token here
TOKEN = '6663036335:AAFYeRj99HAC6B8rD1cab04F_WpUr6pwxXE'

# Initialize the updater
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Define a command handler function
def start(update, context):
    update.message.reply_text('Hello! I am your Telegram bot.')

# Register the command handler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Run the bot
if __name__ == '__main__':
    updater.start_polling()
    updater.idle()
