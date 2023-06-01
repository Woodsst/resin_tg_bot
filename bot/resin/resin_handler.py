import enum

from telebot import types
from telebot.types import Message

from users import User


class ResinMenu(enum.Enum):
    resin_enter_form = "s"
    buttons = "Смола"
    resin = "Кол-во смолы"
    resin_enter = "Задать значение"


async def resin_buttons(message: Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_resin = types.KeyboardButton("Кол-во смолы")
    btn_treasure_resident = types.KeyboardButton("Задать значение")
    btn_menu = types.KeyboardButton("/Меню")
    markup.add(btn_menu, btn_resin, btn_treasure_resident)
    await bot.send_message(
        message.chat.id,
        text="Выберите необходимые данные".format(message.from_user),
        reply_markup=markup,
    )


@bot.message_handler()
async def resin_buttons_work(message: Message):
    if message.text == ResinMenu.resin_enter.value:
        await bot.send_message(
            chat_id=message.chat.id, text="Введите - s <кол-во смолы>"
        )
        user.resin_counter_thread = False
    if message.text == ResinMenu.resin_buttons.value:
        await resin_buttons(message)
    if message.text.split(" ")[0] == ResinMenu.resin_enter_form.value:
        try:
            resin = int(message.text.split(" ")[1])
        except TypeError:
            await bot.send_message(
                chat_id=message.chat.id,
                text="Используйте форму s <кол-во смолы>",
            )
            return
        await user.resin_worker(resin, bot, message)
    if message.text == ResinMenu.resin.value:
        await bot.send_message(chat_id=message.chat.id, text=user.resin)
