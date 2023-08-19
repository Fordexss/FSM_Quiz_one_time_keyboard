from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

change_data = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ім'я"),
         KeyboardButton(text="Електронна пошта"),
         KeyboardButton(text="Вік")]
    ],
    resize_keyboard=True
)
