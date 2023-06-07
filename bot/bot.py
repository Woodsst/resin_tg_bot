from os import getenv
from typing import Optional

from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message

from bot.menu import menu, Menu
from bot.messages import start_message
from bot.parametric_converter.converter_handler import (
    ConverterMenu,
    converter_buttons,
    converter_buttons_work,
)
from bot.resident_treasure.treasure_handler import (
    treasure_buttons,
    TreasureMenu,
    treasure_buttons_work,
)
from bot.resin.resin_handler import ResinMenu, resin_buttons, resin_buttons_work
from log import logger
from users import users, User


bot = AsyncTeleBot(
    getenv("TOKEN", "6290030549:AAF9pOX40vz4bW6NfkZKL3nki8X74YtdpTA")
)


@bot.message_handler(commands=["Меню", "start"])
async def start(message: Message):
    """Основное меню."""
    user = User(message.chat.id, message.from_user.username)
    user_in_work: User = users.get(user.id)
    if user_in_work is None:
        users[user.id] = user
        logger.info(
            f"add user {user.id, user.name}\nusers count = {len(users)}"
        )
    await menu(message, bot)
    if message.text == "/start":
        await bot.send_message(
            message.chat.id,
            text=start_message
        )


@bot.message_handler()
async def work(message: Message):
    logger.info(
        f"user {message.from_user.username} send request - {message.text}"
    )
    user: Optional[User] = users.get(message.chat.id)

    if message.text == Menu.menu.value:
        await menu(message, bot)

    if message.text == ResinMenu.buttons.value:
        await resin_buttons(message, bot)
    await resin_buttons_work(message, bot=bot, user=user)

    if message.text == TreasureMenu.buttons.value:
        await treasure_buttons(message, bot)
    await treasure_buttons_work(message, user, bot)

    if message.text == ConverterMenu.buttons.value:
        await converter_buttons(message, bot)
    await converter_buttons_work(message, bot, user)
