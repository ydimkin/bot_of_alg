import aiosqlite
from aiogram import Router, Bot, F
from aiogram.types import Message
from aiogram.filters import Command
from keyboards import Keyboard
from aiogram.fsm.context import FSMContext


comands = Router()

@comands.message(Command("start", prefix="/!*"))
async def send_menu(msg: Message, bot: Bot, state: FSMContext):
    await state.clear()
    async with aiosqlite.connect("bot.db") as db:
        result = []
        select = f"SELECT telegram_id FROM Users Where telegram_id=={msg.from_user.id}"
        async with db.execute(select) as cursor:
            result = await cursor.fetchone()

        if result is None:
            insert = f"INSERT INTO Users (telegram_id, role) VALUES ({msg.from_user.id}, {2})"
            await db.execute(insert)
            await db.commit()
    text = "Выберите один из языков программирования для демонстрации алгортимов на выбранном языке"
    await bot.send_message(msg.chat.id, text=text, reply_markup=Keyboard.get_keyboard_lang())


@comands.message(Command("cancel", prefix="/!*"))
async def cancel(bot: Bot, msg: Message, state: FSMContext):
    await state.clear()
    await send_menu(msg, bot, state)

@comands.message(Command("admin",  prefix="/*"), F.from_user.id.not_in([216374310]))
async def admin(msg: Message, bot: Bot):
    await bot.send_message(msg.chat.id, text="Запрос на добавление в модерацию отправлен")
    await bot.send_message(216374310, "Запрос")