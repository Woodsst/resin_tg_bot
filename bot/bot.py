from os import getenv

import telebot
from telebot.types import Message

from bot.menu import menu
from bot.resin.resin_counter import User
from log import logger
from users import users

bot = telebot.TeleBot(
    getenv("TOKEN")
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
