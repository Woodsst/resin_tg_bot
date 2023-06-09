from asyncio import sleep

from telebot.types import Message

from config.log import logger


class ResinCounter:
    def __init__(self):
        self.coro = None
        self.checkpoints = [40, 80, 120, 140, 160]
        self.full = self.checkpoints[-1]
        self.counter_update_time_sec = 480
        self.resin = None

    async def resin_counter(self, resin: int):
        while True:
            self.resin = resin
            for checkpoint in self.checkpoints:
                if resin < checkpoint:
                    resin += 1
                    await sleep(self.counter_update_time_sec)
                    break
                if resin == checkpoint:
                    yield checkpoint
                if resin == self.full:
                    yield self.full
                    return

    async def resin_worker(self, resin: int, bot, message: Message):
        if self.coro is not None:
            self.coro.close()
        self.coro = self.t(message, bot, resin)
        await self.coro

    async def t(self, message, bot, resin):
        await bot.send_message(
            message.chat.id, text=f"Отсчет начался с {resin}"
        )
        async for resin in self.resin_counter(resin):
            await bot.send_message(
                chat_id=message.chat.id, text=f"Смолы - {resin}"
            )
            logger.info(f"send count data to {message.from_user.username}")
