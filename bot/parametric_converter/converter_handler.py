import enum

from telebot import types
from telebot.types import Message

from bot.menu import Menu
from users import User


class ConverterMenu(enum.Enum):
    update = "Обновить"
    start = "Запустить"
    value_ = "Оставшееся время"
    buttons = "Параметрический преобразователь"

async def converter_buttons(message: Message, bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_time = types.KeyboardButton(ConverterMenu.value_.value)
    btn_start = types.KeyboardButton(ConverterMenu.start.value)
    btn_menu = types.KeyboardButton(Menu.menu.value)
    btn_update = types.KeyboardButton(ConverterMenu.update.value)
    markup.add(btn_menu, btn_update, btn_start, btn_time)
    await bot.send_message(
        message.chat.id,
        text="Выберите необходимые данные".format(message.from_user),
        reply_markup=markup,
    )

async def converter_buttons_work(message: Message, bot, user: User):
    if message.text == ConverterMenu.start.value:
        pass

    if message.text == ConverterMenu.value_.value:
        pass

    if message.text == ConverterMenu.update.value:
        pass
