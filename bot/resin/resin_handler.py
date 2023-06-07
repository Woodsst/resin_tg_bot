import enum

from telebot import types
from telebot.types import Message

from bot.resin.resin_messages import (
    message_for_resin_menu,
    message_for_enter_resin_counter,
    incorrect_request_resin_counter,
)
from users import User


class ResinMenu(enum.Enum):
    resin_enter_form = "s"
    buttons = "Смола"
    resin = "Кол-во смолы"
    resin_enter = "Задать значение"


async def resin_buttons(message: Message, bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_resin = types.KeyboardButton(ResinMenu.resin.value)
    btn_treasure_resident = types.KeyboardButton(ResinMenu.resin_enter.value)
    btn_menu = types.KeyboardButton(ResinMenu.buttons.value)
    markup.add(btn_menu, btn_resin, btn_treasure_resident)
    await bot.send_message(
        message.chat.id,
        text=message_for_resin_menu,
        reply_markup=markup,
    )


async def resin_buttons_work(message: Message, bot, user: User):
    if message.text == ResinMenu.resin_enter.value:
        await bot.send_message(
            chat_id=message.chat.id, text=message_for_enter_resin_counter
        )
    if message.text.split(" ")[0] == ResinMenu.resin_enter_form.value:
        try:
            resin = int(message.text.split(" ")[1])
        except TypeError:
            await bot.send_message(
                chat_id=message.chat.id,
                text=incorrect_request_resin_counter,
            )
            return
        await user.resin_counter.resin_worker(resin, bot, message)
    if message.text == ResinMenu.resin.value:
        await bot.send_message(
            chat_id=message.chat.id, text=user.resin_counter.resin
        )
