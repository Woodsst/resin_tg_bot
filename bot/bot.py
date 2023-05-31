from os import getenv
from typing import Optional

import telebot
from telebot.types import Message

from bot.menu import menu, Menu
from bot.resident_treasure.treasure_handler import (
    treasure_buttons,
    TreasureMenu,
    treasure_buttons_work,
)
from bot.resin.resin_handler import ResinMenu, resin_buttons, resin_buttons_work
from log import logger
from users import users, User

bot = telebot.TeleBot(
    getenv("TOKEN", "6290030549:AAF9pOX40vz4bW6NfkZKL3nki8X74YtdpTA")
)


@bot.message_handler(commands=["Меню", "start"])
def start(message: Message):
    """Основное меню."""
    user = User(message.chat.id, message.from_user.username)
    user_in_work: User = users.get(user.id)
    if user_in_work is None:
        users[user.id] = user
        logger.info(
            f"add user {user.id, user.name}\nusers count = {len(users)}"
        )
    menu(message, bot)
    if message.text == "/start":
        bot.send_message(
            message.chat.id,
            "Привет, это бот помошник для Геншина, "
            "тут ты сможешь задавать и отслеживать состояния своих сокровищ",
        )


@bot.message_handler()
def work(message: Message):
    logger.info(
        f"user {message.from_user.username} send request - {message.text}"
    )
    user: Optional[User] = users.get(message.chat.id)

    if message.text == Menu.menu.value:
        menu(message, bot)

    if message.text == ResinMenu.buttons.value:
        resin_buttons(message, bot)
    resin_buttons_work(message, user, bot)

    if message.text == TreasureMenu.buttons.value:
        treasure_buttons(message, bot)
    treasure_buttons_work(message, user, bot)
