from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from lexicon.lexicon import KEYBOARDS, BOOKMARKS_KB

def user_kb(keyb):
    kb = ReplyKeyboardBuilder()

    buttons = [KeyboardButton(text=f'{btn}') for btn in KEYBOARDS[keyb]]

    keyboard = kb.row(*buttons, width=1)

    return keyboard.as_markup(resize_keyboard = True, one_time_keyboard =True)

def inline_user_kb(type_kb):

    kb = InlineKeyboardBuilder()


    if type_kb == 'main':
        buttons = [InlineKeyboardButton(text=f'{btn}', callback_data=f'{KEYBOARDS[btn]}') for btn in KEYBOARDS['pagination']]
        save_btn = [InlineKeyboardButton(text=KEYBOARDS['main'], callback_data='save')]
        kb.row(*buttons, width=2)
        kb.row(*save_btn, width=1)
    elif type_kb == 'bookmarks':
        buttons = [InlineKeyboardButton(text=f'{btn}', callback_data=f'{BOOKMARKS_KB[btn]}') for btn in BOOKMARKS_KB['pagination']]
        delete_btn = [InlineKeyboardButton(text=KEYBOARDS['bookmarks'], callback_data='delete')]
        kb.row(*buttons, width=2)
        kb.row(*delete_btn, width=1)

    return kb.as_markup()