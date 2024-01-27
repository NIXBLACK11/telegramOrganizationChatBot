from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

import mongoOp
import inter

loginRequest = False
TOKEN: Final= '6663036335:AAFYeRj99HAC6B8rD1cab04F_WpUr6pwxXE'
BOT_USERNAME = '@Test123manubot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response: str = "Hello! Thanks for chatting with me! I am NIMBLE and I am here to help you regarding your bank information!"
    if mongoOp.userExists(update.message.chat.id):
        response+="You have been successfully logged in"
    else:
        response+="Enter /login to login"
    await update.message.reply_text(response)

async def login_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text: str = update.message.text
    loginRequest = True
    await update.message.reply_text("Enter your credentials in format\nusername password")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    response: str = ""

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if loginRequest:
        if mongoOp.login(update.message.chat.id, text):
            response = "Successfully logged in"
        else:
            response = "Invalid credentials or format"
    else:
        response = inter.response(text, update.message.chat.id)

    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('login', login_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Pooling...')
    app.run_polling(poll_interval=1)