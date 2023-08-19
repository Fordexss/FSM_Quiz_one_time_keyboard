from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default import change_data
from loader import dp
from states.flow import Flow


@dp.message_handler(commands="register")
async def bot_reg_name(message: types.Message):
    await Flow.Register_State_Name.set()
    await message.answer("Напишіть ім'я користувача")


@dp.message_handler(state=Flow.Register_State_Name)
async def bot_reg_mail(message: types.Message, state: FSMContext):
    await Flow.Register_State_Mail.set()
    async with state.proxy() as data:
        data["name"] = message.text
    await message.answer("Напишіть електрону пошту користувача")


@dp.message_handler(state=Flow.Register_State_Mail)
async def bot_reg_age(message: types.Message, state: FSMContext):
    await Flow.Register_State_Age.set()
    async with state.proxy() as data:
        data["mail"] = message.text
    await message.answer("Напишіть вік користувача")


@dp.message_handler(state=Flow.Register_State_Age)
async def bot_reg_age(message: types.Message, state: FSMContext):
    await Flow.Registred_State.set()
    async with state.proxy() as data:
        data["age"] = message.text
    await message.answer("Ви успішно зарееструвались")
    await state.finish()


