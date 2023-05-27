from os import getenv

import telebot
from telebot import types
from telebot.types import Message

from bot.resin.resin_counter import User
from log import logger
from users import users

bot = telebot.TeleBot(getenv("TOKEN"))


@bot.message_handler(commands=['start'])
def start(message: Message):
    """Основное меню."""
    user = User(message.chat.id, message.from_user.username)
    user_in_work: User = users.get(user.id)
    if user_in_work is None:
        users[user.id] = user
        logger.info(f"add user {user.id, user.name}\nusers count = {len(users)}")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_resin = types.KeyboardButton("Смола")
    btn_treasure_resident = types.KeyboardButton("Сокровища обители")
    btn_parameter_converter = types.KeyboardButton("Параметрический преобразователь")
    markup.add(btn_resin, btn_parameter_converter, btn_treasure_resident)
    bot.send_message(message.chat.id,
                     text="Выберите необходимые данные".format(
                         message.from_user), reply_markup=markup)
