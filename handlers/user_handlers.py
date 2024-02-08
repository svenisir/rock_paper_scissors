import logging

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU
from keyboards.keyboard import get_game_kb, get_invite_kb
from services.services import get_bot_choice, get_winner

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    logging.warning('Start command')
    await message.answer(
        text=LEXICON_RU['/start'],
        reply_markup=get_invite_kb()
    )


@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    logging.warning('Help command')
    await message.answer(
        text=LEXICON_RU['/help'],
        reply_markup=get_invite_kb()
    )


@router.message(F.text == LEXICON_RU['yes_button'])
async def process_yes_answer(message: Message):
    logging.warning('Start game')
    await message.answer(
        text=LEXICON_RU['yes'],
        reply_markup=get_game_kb()
    )


@router.message(F.text == LEXICON_RU['no_button'])
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU['no'])


@router.message(F.text.in_([LEXICON_RU['rock'],
                            LEXICON_RU['paper'],
                            LEXICON_RU['scissors']]))
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON_RU["bot_choice"]} '
                              f'- {LEXICON_RU[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(
        text=LEXICON_RU[winner],
        reply_markup=get_game_kb()
    )
