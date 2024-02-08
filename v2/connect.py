import os
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

import mongoOp
import inter

from dotenv import load_dotenv

loginRequest = False

TOKEN: Final = os.getenv("TELEGRAM_API")
BOT_USERNAME: Final = os.getenv("BOT_USERNAME")

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response: str = "Hello! Thanks for chatting with me! I am NIMBLE and I am here to help you regarding your bank information!"
    if mongoOp.userExists(update.message.chat.id):
        response+="\nYou have been successfully logged in"
    else:
        response+="\nEnter /login to login"
    await update.message.reply_text(response)

async def login_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global loginRequest
    text: str = update.message.text
    loginRequest = True
    await update.message.reply_text("Enter your credentials in format\nusername password")

async def logout_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response: str = ""
    if mongoOp.userExists(update.message.chat.id):
        if mongoOp.logout(update.message.chat.id):
            response = "Successfully logged out"
        else:
            response = "Unable to logout"
    else:
        response = "You are not logged in!!"
    
    print('Bot:', response)
    await update.message.reply_text(response)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global loginRequest
    message_type: str = update.message.chat.type
    text: str = update.message.text
    response: str = ""

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if loginRequest:
        try:
            [username, password] = text.split(" ")
            ifNew = mongoOp.ifNewCred(update.message.chat.id, text)
            successLogin = mongoOp.login(update.message.chat.id, text)

            if ifNew and successLogin:
                response = response+"You will be logged out from previous account\nSuccessfully logged in"
                loginRequest = False
            elif ifNew and not successLogin:
                response = "Invalid Credentials\nRetry"
            elif not ifNew and successLogin:
                response = "Already logged in"
                loginRequest = False
        except ValueError:
            response = response+"Invalid credentials\nTry again use format\nusername password"
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