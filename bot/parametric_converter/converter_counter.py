from asyncio import sleep
from datetime import timedelta

from telebot.types import Message


class ConverterCounter:
    WEAK = 604800

    def __init__(self):
        self.converter_check_time_sec = 3600
        self.converter_ready = 0
        self.coro = None
        self.weak_sec = self.WEAK

    async def counter(self, bot, message: Message):
        """Параметрический преобразователь - отметить когда бъёшь,
        откат 7 дней. Через 7 дней можно бить. (тоже булево? )
        оповещение только через неделю с момента нажатия кнопки
        что ты его побил.
        ну и можно кнопку посмотреть когдао ткатится
        """
        while True:
            await sleep(self.converter_check_time_sec)
            self.weak_sec -= self.converter_check_time_sec
            if self.weak_sec <= self.converter_ready:
                await bot.send_message(
                    text=f"Параметрический преобразователь снова доступен",
                    chat_id=message.chat.id,
                )
                self.weak_sec = self.WEAK
                return

    async def run(self, bot, message: Message):
        if self.coro is not None:
            self.coro.close()
            self.converter_ready = 0
        self.coro = self.counter(bot, message)
        await self.coro

    async def timer_progress(self, bot, message: Message):
        await bot.send_message(
            text=timedelta(seconds=self.weak_sec), chat_id=message.chat.id
        )

    async def update(self, bot, message: Message):
        self.weak_sec = self.WEAK
        await self.run(bot, message)
