# Telegram NLP Chat Bot

The Telegram NLP chat bot is designed to understand and respond to natural language input from users on the Telegram platform. It uses NLP to analyze the user's message and determine what action should be taken in response. For example, if the user asks for the weather in a certain location, the bot will use an NLP model to extract the location and then retrieve weather information using an API.

To store data related to user conversations and other information, the bot uses MongoDB, a popular NoSQL database. MongoDB is a document-oriented database that stores data in a flexible, JSON-like format, which makes it well-suited for handling unstructured data like text messages.

Finally, the bot is Dockerized for easy deployment and management. Docker allows you to package your application along with all its dependencies into a single container, which can be deployed to any environment that supports Docker. This makes it easy to set up and manage the bot on different servers or cloud platforms without having to worry about dependencies or compatibility issues.

Overall, the combination of NLP, MongoDB, and Docker makes for a powerful and flexible chat bot that can be easily deployed and scaled to handle a large number of users and conversations.

## Requirements
- Python 3.6 or higher
- Telegram API token
- MongoDB instance
- Docker

## Installation
- Clone this repository and navigate to the project directory.

- Install the required Python packages by running the following command:

    pip install -r requirements.txt

- Create a new Telegram bot by following the instructions in the Telegram Bot documentation.

- Create a MongoDB instance and obtain the connection URL.

- Create a .env file in the root directory of the project and set the following environment variables:

    TELEGRAM_API_TOKEN=<Your Telegram API token>
    MONGODB_URL=<Your MongoDB connection URL>

## Usage
To start the chat bot, run the following command:

    python bot.py

## Docker
To build the Docker image, run the following command:

    docker build -t telegram-nlp-bot .

To start the Docker container, run the following command:

    docker run -d --env-file .env telegram-nlp-bot
