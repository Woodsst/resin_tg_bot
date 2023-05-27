from threading import Thread

from telebot import types
from telebot.types import Message

from bot.resin.resin_counter import User
from log import logger

from bot.bot import bot, users


@bot.message_handler()
def take_resin(message: Message):
    if message.text == "Задать значение":
        bot.send_message(chat_id=message.chat.id, text="Введите - Смола <колличество смолы>")
    logger.info(f"user {message.from_user.username} send request - {message.text}")
    user = User(message.chat.id, message.from_user.username)
    counter_in_work: User = users.get(user.id)
    if counter_in_work is not None:
        if message.text == "stop":
            counter_in_work.status = False
            logger.info(f"user {user.id} stop count work")
            return
        counter_in_work.status = False
    users[user.id] = user
    logger.info(f"users count = {len(users)}")
    thread = Thread(target=counter_thread, args=(message, user))
    thread.run()


def counter_thread(message: Message, resin: User):
    try:
        for resin in resin.resin_counter(int(message.text)):
            bot.send_message(chat_id=message.chat.id, text=resin)
            logger.info(f"send count data to {message.from_user.username}")
    except TypeError as e:
        logger.warning(e)
        return


@bot.message_handler(content_types=["text"])
def resin(message: Message):
    """Действия при нажатии на кнопку 'Смола'."""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_resin = types.KeyboardButton("Кол-во смолы")
    btn_treasure_resident = types.KeyboardButton("Задать значение")
    markup.add(btn_resin, btn_treasure_resident)
    bot.send_message(message.chat.id,
                     text="Выберите необходимые данные".format(
                         message.from_user), reply_markup=markup)

