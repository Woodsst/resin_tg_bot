import telebot
from telebot.types import Message
from os import getenv

bot = telebot.TeleBot(getenv("TOKEN"))


@bot.message_handler()
def send_welcome(message: Message):
    bot.send_message(chat_id=message.chat.id, text=message.text)
