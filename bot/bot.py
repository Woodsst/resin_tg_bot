from threading import Thread

import telebot
from telebot.types import Message
from os import getenv
from bot.resin_counter import User

bot = telebot.TeleBot(getenv("TOKEN"))

users = {}


def counter_thread(message: Message, resin: User):
    try:
        for resin in resin.resin_counter(int(message.text)):
            bot.send_message(chat_id=message.chat.id, text=resin)
    except TypeError:
        return


@bot.message_handler()
def send_welcome(message: Message):
    user = User(message.chat.id)
    counter_in_work: User = users.get(user.id)
    if counter_in_work is not None:
        if message.text == "stop":
            counter_in_work.status = False
            return
        counter_in_work.status = False
    users[user.id] = user
    thread = Thread(target=counter_thread, args=(message, user))
    thread.run()
