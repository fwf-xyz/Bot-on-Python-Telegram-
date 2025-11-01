from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                        InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='📝Внести данные')],
                            [KeyboardButton(text='📊Статистика'), KeyboardButton(text='О боте')]],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню')

settings = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Tesseract', url='https://t.me/cube_4d')]])