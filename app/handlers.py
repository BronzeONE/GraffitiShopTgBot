from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


import app.keyboards as kb


router= Router()


class Register(StatesGroup):
    name = State()
    age = State()
    phonenumber = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('hello bro!', reply_markup= kb.main)
    await message.reply('как дела?)')

@router.message(Command('Help'))
async def cmd_help(message: Message):
    await message.answer('SOS нам нужна помощь здесь!')




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

@router.message(Command("register"))
async def register(message: Message, state: FSMContext ):
    await state.set_state(Register.name)
    await message.answer('Введите ваше имя')


@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.age)
    await message.answer('Введите ваш возраст')



@router.message(Register.age)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Register.phonenumber)
    await message.answer('Введите Phonenumber', reply_markup=kb.get_phonenuber)


@router.message(Register.phonenumber,F.contact)
async def register_phonenumber(message: Message, state: FSMContext):
    await state.update_data(phonenumber=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f'ваше имя{data["name"]}\nВаш возраст: {data["age"]} \nНомер {data["phonenumber"]}')
    await state.clear


