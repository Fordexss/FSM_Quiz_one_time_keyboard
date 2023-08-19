from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default import dynamic_reply_kb
from loader import dp
from states.quiz import Quiz

quiz_button = [
    ['Румунія', 'Ватикан', 'Монако', 'Сан-Марино', 'Науру'],
    ['Оттава', 'Нью-Йорк', 'Вашингтон', 'Сан-Франциско', 'Орландо'],
    ['Бурдж Халіф', 'Шанхайська Вежа', 'Абрадж аль-Бейт', 'Тайбей 101', 'Чайна Цзунь']
]
correct_answers = {
    0: 'Ватикан',
    1: 'Вашингтон',
    2: 'Бурдж Халіф'
}


@dp.message_handler(commands="quiz")
async def bot_quiz_start_game(message: types.Message):
    await Quiz.Start_quiz.set()
    await message.answer("Питання №1\n"
                         "Яка найменша країна в світі?:", reply_markup=dynamic_reply_kb(quiz_button[0]))


@dp.message_handler(state=Quiz.Start_quiz)
async def bot_second_question(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['answer_first'] = message.text
    await Quiz.Second_Question.set()
    await message.answer("Ваша відповідь зарахована")
    await message.answer("Питання №2\n"
                         "Яка столиця США?:", reply_markup=dynamic_reply_kb(quiz_button[1]))


@dp.message_handler(state=Quiz.Second_Question)
async def bot_third_question(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['answer_second'] = message.text
    await Quiz.Third_Question.set()
    await message.answer("Ваша відповідь зарахована")
    await message.answer("Питання №3\n"
                         "Яка найвища споруда, створена людиною?:", reply_markup=dynamic_reply_kb(quiz_button[2]))


@dp.message_handler(state=Quiz.Third_Question)
async def bot_finish(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        async with state.proxy() as data:
            data['answer_third'] = message.text
            counter = 0
            if data['answer_first'] == correct_answers[0]:  # you can also get the value from quiz_button[0][1]. This example applies to everyone. Thanks for that date option,L1nk3rrr
                counter += 1
            if data['answer_second'] == correct_answers[1]:
                counter += 1
            if data['answer_third'] == correct_answers[2]:
                counter += 1
    await Quiz.Finished_quiz.set()
    await message.answer(f"Ви успішно пройшли тест! Кількість правильних відповідей: {counter}")
    await state.finish()
