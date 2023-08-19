from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("register", "Зарееструватися"),
            types.BotCommand("editdata", "Змінити данні"),
            types.BotCommand("quiz", "Почати міні-тест")
        ]
    )
