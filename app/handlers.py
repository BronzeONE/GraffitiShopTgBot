from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import app.keyboards as kb


router= Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('hello bro!', reply_markup= kb.main)
    await message.reply('как дела?)')

@router.message(Command('Help'))
async def cmd_help(message: Message):
    await message.answer('SOS нам нужна помощь здесь')




@router.message(F.text == 'каталог')
async def catalog (message: Message):
    await message.answer("выбери, нужный раздел", reply_markup=kb.catalog)

@router.callback_query(F.data == 'bandb')
async def acsesories (callback: CallbackQuery):
    await callback.answer('уведомление', show_alert=True)
    await callback.message.answer('вы выбрали раздел <всякое разное>')

@router.callback_query(F.data == 'paint')
async def bombing (callback: CallbackQuery):
    await callback.message.answer('вы выбрали раздел <краска>')

@router.callback_query(F.data == 'markers')
async def taging (callback: CallbackQuery):
    await callback.message.answer('вы выбрали раздел <маркеры>')

