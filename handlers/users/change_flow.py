from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default import change_data
from loader import dp
from states.flow import Flow


@dp.message_handler(commands="editdata")
async def bot_edit(message: types.Message):
    await Flow.Edit_State_Name.set()
    await message.answer("Що саме ви хочете змінити?", reply_markup=change_data)


@dp.message_handler(text="Ім'я", state=Flow.Edit_State_Name)
async def bot_edit_name(message: types.Message, state: FSMContext):
    await Flow.Edit_State_Name2.set()
    await message.answer("Поширте нове ім'я")


@dp.message_handler(text="Електронна пошта", state=Flow.Edit_State_Name)
async def bot_edit_mail(message: types.Message, state: FSMContext):
    await Flow.Edit_State_Mail2.set()
    await message.answer("Поширте нову електронну пошту")


@dp.message_handler(text="Вік", state=Flow.Edit_State_Name)
async def bot_edit_age(message: types.Message, state: FSMContext):
    await Flow.Edit_State_Age2.set()
    await message.answer("Поширте новий вік")


@dp.message_handler(state=Flow.Edit_State_Name2)
async def bot_edit_name2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await message.answer("Ви успішно змінили ім'я")
    await state.finish()


@dp.message_handler(state=Flow.Edit_State_Mail2)
async def bot_edit_mail2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["mail"] = message.text
    await message.answer("Ви успішно змінили пошту")
    await state.finish()


@dp.message_handler(state=Flow.Edit_State_Age2)
async def bot_edit_age2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["age"] = message.text
    await message.answer("Ви успішно змінили вік")
    await state.finish()
