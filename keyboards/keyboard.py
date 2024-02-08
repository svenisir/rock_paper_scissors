from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton
from aiogram.types import ReplyKeyboardMarkup
from lexicon.lexicon import LEXICON_RU

# Кнопки приглашения в игру
button_yes = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no = KeyboardButton(text=LEXICON_RU['no_button'])

yes_no_kb_builder = ReplyKeyboardBuilder()

yes_no_kb_builder.row(button_yes, button_no, width=2)

yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

# Кнопки игровой клавиатуры
btn_1 = KeyboardButton(text=LEXICON_RU['rock'])
btn_2 = KeyboardButton(text=LEXICON_RU['paper'])
btn_3 = KeyboardButton(text=LEXICON_RU['scissor'])

btn_s = [btn_1, btn_2, btn_3]

game_kb_builder = ReplyKeyboardBuilder()

game_kb_builder.row(*btn_s, width=1)

game_kb = game_kb_builder.as_markup(resize_keyboard=True)
