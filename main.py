from bot.bot import bot
from bot.resin import resin_handler
from log import logger

if __name__ == "__main__":
    logger.info("start")
    bot.infinity_polling()
