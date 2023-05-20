from threading import Thread

import telebot
from telebot.types import Message
from os import getenv
from resin_counter import Resin

bot = telebot.TeleBot(getenv("TOKEN"))

users = {}


def counter_thread(message: Message, resin: Resin):
    for resin in resin.resin_counter(int(message.text)):
        bot.send_message(chat_id=message.chat.id, text=resin)


@bot.message_handler()
def send_welcome(message: Message):
    user = Resin(message.chat.id)
    counter_in_work = users.get(user.id)
    if counter_in_work is not None:
        counter_in_work.status = False
    users[user.id] = user
    thread = Thread(target=counter_thread, args=(message, user))
    thread.run()
