import time
from threading import Thread

from telebot.types import Message
from log import logger


class User:

    def __init__(self, chat_id: int, username: str):
        self.name = username
        self.id = chat_id
        self.resin_counter_thread = True
        self.checkpoints = [40, 80, 120, 140, 160]
        self.full = self.checkpoints[-1]
        self.counter_update_time_sec = 0.1
        self.resin = None

    def resin_counter(self, resin: int):
        while self.resin_counter_thread is True:
            self.resin = resin
            for i in self.checkpoints:
                if resin < i:
                    resin += 1
                    logger.info(f"{self.id} resin update {resin}")
                    time.sleep(self.counter_update_time_sec)
                    break
                if resin == i:
                    yield i
                if resin == self.full:
                    yield self.full
                    resin = 0
                    self.resin_counter_thread = False
                    break

    def resin_worker(self, resin: int, bot, message: Message):
        bot.send_message(message.chat.id, text=f"Отсчет начался с {resin}")
        self.resin_counter_thread = True
        for resin in self.resin_counter(resin):
            bot.send_message(chat_id=message.chat.id, text=resin)
            logger.info(f"send count data to {message.from_user.username}")

    def resin_thread_start(self, resin: int, bot, message):
        thread = Thread(target=self.resin_worker, args=(resin, bot, message))
        thread.run()
