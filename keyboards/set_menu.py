from aiogram import Bot
from aiogram.types import BotCommand
from lexicon.lexicon import LEXICON_COMMANDS_RU


async def set_main_menu(bot: Bot) -> None:
    main_menu_command = [
        BotCommand(
            command=command,
            description=description
        )
        for command, description in LEXICON_COMMANDS_RU.items()
    ]
    await bot.set_my_commands(main_menu_command)
