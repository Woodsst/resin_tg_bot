from typing import Optional

from telebot import types
from telebot.types import Message

from bot.bot import bot
from bot.menu import menu
from users import users
from bot.resin.resin_counter import User
from log import logger


def resin_buttons(message: Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_resin = types.KeyboardButton("Кол-во смолы")
    btn_treasure_resident = types.KeyboardButton("Задать значение")
    btn_menu = types.KeyboardButton("Вернуться в меню")
    markup.add(btn_menu, btn_resin, btn_treasure_resident)
    bot.send_message(message.chat.id,
                     text="Выберите необходимые данные".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler()
def resin_buttons_work(message: Message):
    logger.info(f"user {message.from_user.username} send request - {message.text}")
    user: Optional[User] = users.get(message.chat.id)
    if message.text == "Вернуться в меню":
        menu(message, bot)
    if message.text == "Задать значение":
        bot.send_message(chat_id=message.chat.id, text="Введите - s <кол-во смолы>")
        user.resin_counter_thread = False
    if message.text == "Смола":
        resin_buttons(message)
    if message.text.split(" ")[0] == "s":
        try:
            resin = int(message.text.split(" ")[1])
        except TypeError:
            bot.send_message(chat_id=message.chat.id, text="Используйте форму s <кол-во смолы>")
            return
        if user.resin_counter_thread is True:
            user.resin_counter_thread = False
        user.resin_thread_start(resin, bot, message)
    if message.text == "Кол-во смолы":
        bot.send_message(chat_id=message.chat.id, text=user.resin)
