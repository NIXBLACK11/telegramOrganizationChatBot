import os
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

import mongoOp
import inter
from languageChange import supported_languages, translate_text, get_code, supported_languages_dict

from dotenv import load_dotenv

loginRequest = False
setLanguage = False
language = "en"

TOKEN: Final = os.getenv("TELEGRAM_API")
BOT_USERNAME: Final = os.getenv("BOT_USERNAME")

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response: str = "Hello! Thanks for chatting with me! I am NIMBLE and I am here to help you regarding your bank information!"
    if mongoOp.userExists(update.message.chat.id):
        response+="\nYou have been successfully logged in"
    else:
        response+="\nEnter /login to login"
    response = translate_text(response, language)
    await update.message.reply_text(response)

async def login_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global loginRequest
    response: str = "Enter your credentials in format\nusername password"
    text: str = update.message.text
    loginRequest = True
    response = translate_text(response, language)
    await update.message.reply_text(response)

async def logout_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response: str = ""
    if mongoOp.userExists(update.message.chat.id):
        if mongoOp.logout(update.message.chat.id):
            response = "Successfully logged out"
        else:
            response = "Unable to logout"
    else:
        response = "You are not logged in!!"

    response = translate_text(response, language)
    await update.message.reply_text(response)

async def language_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global setLanguage
    text: str = update.message.text
    setLanguage = True
    response: str = "Enter the language you want to set\nThe languages supported are:\n"
    for code, language in supported_languages_dict.items():
        response=response+(f"{code}) {language}\n")
    await update.message.reply_text(response)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global loginRequest
    global setLanguage
    global language
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
    elif setLanguage:
        if text in supported_languages:
            language = get_code(text)
            response = f"Language set to {text}"
            setLanguage = False
        else:
            response = "Invalid language code entered. Please enter a valid language code."
    else:
        response = inter.response(text, update.message.chat.id)
        path = f'monthly_expenditures_{str(update.message.chat.id)}.png'
        if response == path:
            await context.bot.send_photo(update.message.chat.id, photo=open(path, 'rb'))
            os.remove(path)
            return

    response = translate_text(response, language)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('login', login_command))
    app.add_handler(CommandHandler('logout', logout_command))
    app.add_handler(CommandHandler('language', language_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Pooling...')
    app.run_polling(poll_interval=1)