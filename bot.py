import telebot
import os
from flask import Flask

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

# Run bot in background
import threading
threading.Thread(target=bot.infinity_polling).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
