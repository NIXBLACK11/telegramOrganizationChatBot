from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


TOKEN: Final= '6663036335:AAFYeRj99HAC6B8rD1cab04F_WpUr6pwxXE'
BOT_USERNAME = '@Test123manubot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if userExists(update.message.chat.type):
        await update.message.reply_text('Hello! Thanks for chatting with me! I am NIMBLE and I am here to help you regarding your bank information! You have been successfully logged in')
    else
        await update.message.reply_text('Hello! Thanks for chatting with me! I am NIMBLE and I am here to help you regarding your bank information! Enter /login to login')

async def login_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text: str = update.message.text
    print(text)


# def handle_response(text: str) -> str:
#     processed: str = text.lower()

#     return "hello"

# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     message_type: str = update.message.chat.type
#     text: str = update.message.text

#     print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

#     if message_type == 'group':
#         if BOT_USERNAME in text:
#             new_text: str = text.replace(BOT_USERNAME, '').strip()
#             response: str = handle_response(new_text)
#         else:
#             return
#     else:
#         response: str = handle_response(text)

#     print('Bot:', response)
#     await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Pooling...')
    app.run_polling(poll_interval=3)