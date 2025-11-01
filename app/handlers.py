from aiogram import F, Router
from aiogram.types import Message 
from aiogram.filters import CommandStart, Command 

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer_photo(photo='https://davidgoggins.com/wp-content/uploads/2022/02/david_goggins_about.png',
                            caption=f'Приветствую, спартанец! 👋 \n \nКакой вес сегодня поднял на жиме лежа?💪', reply_markup=kb.settings)

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('КНОПКА ПОМОЩИ АКТИВИРОВАНА')

@router.message(F.text == '📝Внести данные')
async def cmd_help(message: Message):
    await message.answer('Данные обновлены')


