#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
from dotenv import load_dotenv
from os import getenv

load_dotenv()

API_TOKEN = getenv("API_TOKEN")

bot = telebot.TeleBot(API_TOKEN)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message: telebot.types.Message):
    if message.via_bot:
        if message.via_bot.username in ["HowYourBot"]:
            bot.delete_message(chat_id=message.chat.id, message_id=message.id)


bot.infinity_polling()
