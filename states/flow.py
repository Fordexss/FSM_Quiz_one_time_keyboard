from aiogram.dispatcher.filters.state import StatesGroup, State


class Flow(StatesGroup):
    Register_State_Name = State()
    Register_State_Mail = State()
    Register_State_Age = State()
    Registred_State = State()
    Edit_State_Name = State()
    Edit_State_Mail = State()
    Edit_State_Age = State()
    Edit_State_Name2 = State()
    Edit_State_Mail2 = State()
    Edit_State_Age2 = State()

