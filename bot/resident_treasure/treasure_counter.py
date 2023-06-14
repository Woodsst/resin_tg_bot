from asyncio import sleep

from telebot.types import Message


class TreasureCounter:
    def __init__(self, update_time_sec: int = 3600):
        self.status = False
        self.full = 2400
        self.update_time_sec = update_time_sec
        self.treasure = 0
        self.treasure_update = 30
        self.coro = None

    async def counter(self):
        while True:
            await sleep(self.update_time_sec)
            self.treasure += self.treasure_update
            if self.treasure >= self.full:
                yield self.full
                return

    async def run(self, bot, message: Message):
        if self.coro is not None:
            self.coro.close()
        self.coro = self.worker(bot, message)
        await self.coro

    async def worker(self, bot, message: Message):
        async for treasure in self.counter():
            if treasure == self.full:
                await bot.send_message(
                    text=f"Копилка сокровищ полна {treasure}",
                    chat_id=message.chat.id,
                )

    async def reload(self, bot, message: Message):
        self.treasure = 0
        await self.run(bot, message)
