from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = 'каталог')],
                                     [KeyboardButton(text = 'корзина')],
                                     [KeyboardButton(text = 'контакты'),
                                     KeyboardButton(text = 'О нас')]],
                           resize_keyboard=True,
                           input_field_placeholder='нажми на кнопку уже (.)(.)')


catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='краска', callback_data='paint')],
    [InlineKeyboardButton(text='всякое разное',callback_data='bandb')],
    [InlineKeyboardButton(text='маркеры',callback_data='markers')]])



get_phonenuber = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='отправить номер',
                                                               request_contact=True)]],
                                                               resize_keyboard=True)