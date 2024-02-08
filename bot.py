import asyncio

from aiogram import Bot, Dispatcher
from handlers import user_handlers, other_handlers
from config_data.config import load_config, Config
from keyboards.set_menu import set_main_menu


async def main() -> None:

    config: Config = load_config()

    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher()

    await set_main_menu(bot)

    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
