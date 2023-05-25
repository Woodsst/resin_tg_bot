from bot.bot import bot
from log import logger

if __name__ == "__main__":
    logger.info("start")
    bot.infinity_polling()
