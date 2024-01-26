from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
# TOKEN = 'YOUR_BOT_TOKEN'
TOKEN = '6663036335:AAFYeRj99HAC6B8rD1cab04F_WpUr6pwxXE'

# Dictionary to store user details (replace with your user details logic)
user_details = {}

# Command to handle user login
def start(update, context):
    user_id = update.message.from_user.id

    # Check if the user is already logged in
    if user_id in user_details:
        context.bot.send_message(chat_id=update.effective_chat.id, text="You are already logged in.")
    else:
        # Temporary logic for user details (replace with your actual logic)
        username = f'user{user_id}'
        email = f'user{user_id}@example.com'

        # Save user details
        user_details[user_id] = {'username': username, 'email': email}

        # Send login details to the user
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Login successful!\nUsername: {username}\nEmail: {email}")

# Command to display user details
def details(update, context):
    user_id = update.message.from_user.id

    # Check if the user is logged in
    if user_id in user_details:
        user_info = user_details[user_id]
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Username: {user_info['username']}\nEmail: {user_info['email']}")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="You are not logged in. Please use /start to log in.")

def main():
    # Create the Updater and pass it your bot's token
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("details", details))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop it
    updater.idle()

if __name__ == '__main__':
    main()
