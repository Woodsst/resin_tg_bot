import enum
from typing import Optional

from telebot import types
from telebot.types import Message

from bot.bot import bot
from bot.menu import menu
from users import users
from bot.resin.resin_counter import User
from log import logger


class ResinMenu(enum.Enum):
    resin_enter_form = "s"
    resin_buttons = "Смола"
    resin = "Кол-во смолы"
    resin_enter = "Задать значение"
    menu_back = "Вернуться в меню"


def resin_buttons(message: Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_resin = types.KeyboardButton("Кол-во смолы")
    btn_treasure_resident = types.KeyboardButton("Задать значение")
    btn_menu = types.KeyboardButton("Вернуться в меню")
    markup.add(btn_menu, btn_resin, btn_treasure_resident)
    bot.send_message(
        message.chat.id,
        text="Выберите необходимые данные".format(message.from_user),
        reply_markup=markup,
    )


@bot.message_handler()
def resin_buttons_work(message: Message):
    logger.info(
        f"user {message.from_user.username} send request - {message.text}"
    )
    user: Optional[User] = users.get(message.chat.id)
    if message.text == ResinMenu.menu_back.value:
        menu(message, bot)
    if message.text == ResinMenu.resin_enter.value:
        bot.send_message(
            chat_id=message.chat.id, text="Введите - s <кол-во смолы>"
        )
        user.resin_counter_thread = False
    if message.text == ResinMenu.resin_buttons.value:
        resin_buttons(message)
    if message.text.split(" ")[0] == ResinMenu.resin_enter_form.value:
        try:
            resin = int(message.text.split(" ")[1])
        except TypeError:
            bot.send_message(
                chat_id=message.chat.id,
                text="Используйте форму s <кол-во смолы>",
            )
            return
        if user.resin_counter_thread is True:
            user.resin_counter_thread = False
        user.resin_thread_start(resin, bot, message)
    if message.text == ResinMenu.resin.value:
        bot.send_message(chat_id=message.chat.id, text=user.resin)
