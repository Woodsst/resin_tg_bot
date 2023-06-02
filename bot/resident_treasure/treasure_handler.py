import enum

from telebot import types
from telebot.types import Message

from bot.bot import Menu
from users import User


class TreasureMenu(enum.Enum):
    buttons = "Сокровища обители"
    start = "Запустить"
    value_ = "Кол-во Сокровищ"
    update = "Обновить"


async def treasure_buttons(message: Message, bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_resin = types.KeyboardButton(TreasureMenu.value_.value)
    btn_treasure_resident = types.KeyboardButton(TreasureMenu.start.value)
    btn_menu = types.KeyboardButton(Menu.menu.value)
    btn_update = types.KeyboardButton(TreasureMenu.update.value)
    markup.add(btn_menu, btn_resin, btn_treasure_resident, btn_update)
    await bot.send_message(
        message.chat.id,
        text="Выберите необходимые данные".format(message.from_user),
        reply_markup=markup,
    )


async def treasure_buttons_work(message: Message, user: User, bot):
    if message.text == TreasureMenu.start.value:
        await user.treasure_counter.run(bot, message)

    if message.text == TreasureMenu.value_.value:
        await bot.send_message(
            text=f"Сокровищ - {user.treasure_counter.treasure}", chat_id=user.id
        )

    if message.text == TreasureMenu.update.value:
        await user.treasure_counter.reload(bot, message)
