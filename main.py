from bot.bot import bot
from log import logger
from asyncio import run

if __name__ == "__main__":
    logger.info("start")
    run(bot.infinity_polling())
