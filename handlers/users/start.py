from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default import change_data
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Що ви хочете змінити?", reply_markup=change_data)



