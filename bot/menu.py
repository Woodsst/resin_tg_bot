import enum

from telebot import types
from telebot.types import Message


class Menu(enum.Enum):
    menu = "/Меню"


async def menu(message: Message, bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_resin = types.KeyboardButton("Смола")
    btn_treasure_resident = types.KeyboardButton("Сокровища обители")
    btn_parameter_converter = types.KeyboardButton(
        "Параметрический преобразователь"
    )
    markup.add(btn_resin, btn_parameter_converter, btn_treasure_resident)
    await bot.send_message(
        message.chat.id,
        text="""
        Основное меню
        """,
        reply_markup=markup,
    )
