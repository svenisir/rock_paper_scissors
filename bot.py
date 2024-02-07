import asyncio
import logging.config

from aiogram import Bot, Dispatcher
from config_data.config import load_config
from logging_settings.logging_settings import logging_config


async def main() -> None:

    config = load_config()

    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    logging.config.dictConfig(logging_config)

    bot.delete_webhook(drop_pending_updates=True)
    dp.run_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
