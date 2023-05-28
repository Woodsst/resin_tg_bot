from telebot import types
from telebot.types import Message


def menu(message: Message, bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_resin = types.KeyboardButton("Смола")
    btn_treasure_resident = types.KeyboardButton("Сокровища обители")
    btn_parameter_converter = types.KeyboardButton(
        "Параметрический преобразователь"
    )
    markup.add(btn_resin, btn_parameter_converter, btn_treasure_resident)
    bot.send_message(
        message.chat.id,
        text="Выберите необходимые данные".format(message.from_user),
        reply_markup=markup,
    )
