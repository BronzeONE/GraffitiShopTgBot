from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


import app.keyboards as kb
import app.database.request as rq


router= Router()


#class Register(StatesGroup):
#    name = State()
#    age = State()
#    phonenumber = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer('hi bro this is a graffiti shop', reply_markup= kb.main)
    


@router.message(F.text == 'каталог')
async def catalog (message: Message):
    await message.answer("выбери, нужный раздел", reply_markup=await kb.categories())

@router.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Выберите товар по категории',
                                  reply_markup=await kb.items(callback.data.split('_')[1]))
    
@router.callback_query(F.data.startswith('item_'))
async def category(callback: CallbackQuery):
    item_data = await rq.get_item(callback.data.split('_')[1])
    await callback.answer('Вы выбрали товар')
    await callback.message.answer(f'Название: {item_data.name}\nОписание: {item_data.description}\nЦена: {item_data.price}$')

#@router.message(Command("register"))
#async def register(message: Message, state: FSMContext ):
#    await state.set_state(Register.name)
#    await message.answer('Введите ваше имя')

#@router.message(Register.name)
#async def register_name(message: Message, state: FSMContext):
#    await state.update_data(name=message.text)
#    await state.set_state(Register.age)
#    await message.answer('Введите ваш возраст')

#@router.message(Register.age)
#async def register_name(message: Message, state: FSMContext):
#    await state.update_data(age=message.text)
#    await state.set_state(Register.phonenumber)
#    await message.answer('Введите Phonenumber', reply_markup=kb.get_phonenuber)


#@router.message(Register.phonenumber,F.contact)
#async def register_phonenumber(message: Message, state: FSMContext):
#    await state.update_data(phonenumber=message.contact.phone_number)
#    data = await state.get_data()
#    await message.answer(f'ваше имя: {data["name"]}\nВаш возраст: {data["age"]} \nНомер: {data["phonenumber"]}')
#    await state.clear