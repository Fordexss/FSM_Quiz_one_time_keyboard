from aiogram.dispatcher.filters.state import StatesGroup, State


class Quiz(StatesGroup):
    Start_quiz = State()
    Second_Question = State()
    Third_Question = State()
    Finished_quiz = State()
