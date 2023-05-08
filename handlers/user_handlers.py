from aiogram import Router

from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.filters import Command, CommandStart, Text

from lexicon.lexicon import LEXICON
from keyboards.keyboards import user_kb, inline_user_kb
from service.service import get_announcement, next_announcement
from data.data import USER_STATUS, USER_CURRENT
from data import db

router = Router()

@router.message(CommandStart())
async def procces_command_start(message: Message):
    await message.answer(text=LEXICON['start'], reply_markup=user_kb('start'))

@router.message(Command(commands='help'))
async def procces_command_help(message: Message):
    await message.answer(text=LEXICON['help'])

@router.message(Command(commands='stop'))
async def procces_command_stop(message: Message):
    try:
        del USER_STATUS[message.from_user.id]
    except KeyError:
        pass

    await message.answer(text=LEXICON['stop'])

@router.message(Command(commands='search'))
async def procces_command_search(message: Message):
    await message.answer(text=LEXICON['start'], reply_markup=user_kb('start'))

@router.message(Text(text='Сначала дешевые'))
async def down_sort(message: Message):
    USER_STATUS[message.from_user.id] = ['down', 0]
    posts = get_announcement(USER_STATUS[message.from_user.id][0])
    await message.answer(text=posts, reply_markup=inline_user_kb('main'))

@router.message(Text(text='Сначала дорогие'))
async def up_sort(message: Message):
    USER_STATUS[message.from_user.id] = ['up', 3214]
    posts = get_announcement(USER_STATUS[message.from_user.id][0])
    await message.answer(text=posts, reply_markup=inline_user_kb('main'))


@router.callback_query(Text(text='forward'))
async def forward_post(callback: CallbackQuery):
    if USER_STATUS[callback.from_user.id][0] == 'up':
        USER_STATUS[callback.from_user.id][1] -= 1
    else:
        USER_STATUS[callback.from_user.id][1] += 1

    next_posts = next_announcement(USER_STATUS[callback.from_user.id][1])
    await callback.message.edit_text(text=next_posts, reply_markup=inline_user_kb('main'))

@router.callback_query(Text(text='backward'))
async def backward_post(callback: CallbackQuery):
    if USER_STATUS[callback.from_user.id][0] == 'up':
        USER_STATUS[callback.from_user.id][1] += 1
    else:
        USER_STATUS[callback.from_user.id][1] -= 1

    next_posts = next_announcement(USER_STATUS[callback.from_user.id][1])
    await callback.message.edit_text(text=next_posts, reply_markup=inline_user_kb('main'))

@router.callback_query(Text(text='save'))
async def save_post(callback: CallbackQuery):
    db.save_post(callback.from_user.id, callback.message.text)
    await callback.answer(text=LEXICON['save'])

@router.message(Command(commands='mybookmarks'))
async def get_bookmarks(message: Message):
    post = db.select_post(message.from_user.id)
    USER_CURRENT[message.from_user.id] = 0
    await message.answer(' '.join(post[0]), reply_markup= inline_user_kb('bookmarks'))

@router.callback_query(Text(text='forward_bookmarks'))
async def next_bookmarks(callback: CallbackQuery):
    USER_CURRENT[callback.from_user.id]+= 1
    post = db.select_post(callback.from_user.id)
    await callback.message.edit_text(''.join(post[USER_CURRENT[callback.from_user.id]]), reply_markup=inline_user_kb('bookmarks'))

@router.callback_query(Text(text='backward_bookmarks'))
async def back_bookmarks(callback: CallbackQuery):
    USER_CURRENT[callback.from_user.id]-= 1
    post = db.select_post(callback.from_user.id)
    await callback.message.edit_text(''.join(post[USER_CURRENT[callback.from_user.id]]), reply_markup=inline_user_kb('bookmarks'))


@router.callback_query(Text(text='delete'))
async def delete_bookmarks(callback: CallbackQuery):
    db.delete_post(callback.from_user.id, callback.message.text)
    post = db.select_post(callback.from_user.id)
    await callback.answer(text=LEXICON['delete'])
    if len(post) > 0:
        await callback.message.edit_text(text=''.join(post[USER_CURRENT[callback.from_user.id]]), reply_markup=inline_user_kb('bookmarks'))
    else:
        await callback.message.edit_text(text=LEXICON['empty'])