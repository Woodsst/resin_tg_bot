import enum

from telebot import types
from telebot.types import Message

from users import User


class ResinMenu(enum.Enum):
    resin_enter_form = "s"
    buttons = "Смола"
    resin = "Кол-во смолы"
    resin_enter = "Задать значение"


def resin_buttons(message: Message, bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_resin = types.KeyboardButton("Кол-во смолы")
    btn_treasure_resident = types.KeyboardButton("Задать значение")
    btn_menu = types.KeyboardButton("/Меню")
    markup.add(btn_menu, btn_resin, btn_treasure_resident)
    bot.send_message(
        message.chat.id,
        text="Выберите необходимые данные".format(message.from_user),
        reply_markup=markup,
    )


def resin_buttons_work(message: Message, user: User, bot):
    if message.text == ResinMenu.resin_enter.value:
        bot.send_message(
            chat_id=message.chat.id, text="Введите - s <кол-во смолы>"
        )
        user.resin_counter_thread = False
    if message.text.split(" ")[0] == ResinMenu.resin_enter_form.value:
        try:
            resin = int(message.text.split(" ")[1])
        except TypeError:
            bot.send_message(
                chat_id=message.chat.id,
                text="Используйте форму s <кол-во смолы>",
            )
            return
        user.update_resin_counter_status()
        user.resin_thread_start(resin, bot, message)
    if message.text == ResinMenu.resin.value:
        bot.send_message(chat_id=message.chat.id, text=user.resin)
