from aiogram import Router, Bot, F
from aiogram.types import Message
from aiogram.filters import Command
from keyboards import Keyboard
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from State import StateMenu
import aiosqlite
from aiogram.filters.state import StateFilter
from aiogram.utils.formatting import Pre
from typing import Dict


_router = Router()

@_router.message(Command("start", prefix="/!*"))
async def send_menu(msg: Message, bot: Bot, state: FSMContext):
    await state.clear()
    text = "Выберите один из языков программирования для демонстрации алгортимов на выбранном языке"
    await bot.send_message(msg.chat.id, text=text, reply_markup=Keyboard.get_keyboard_lang())


@_router.message(Command("cancel", prefix="/!*"))
async def cancel(bot: Bot, msg: Message, state: FSMContext):
    await state.clear()
    await send_menu(msg, bot, state)

@_router.message(Command("admin", prefix="/*"), F.from_user.id.not_in([216374310]))
async def admin(msg: Message, bot: Bot):
    await bot.send_message(msg.chat.id, text="Запрос на добавление в модерацию отправлен")


@_router.callback_query(F.data == "Назад")
async def back(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    print(data)
    if data == {}:
        text = "Выберите один из языков программирования для демонстрации алгортимов на выбранном языке"
        await callback.message.edit_text(text=text, reply_markup=Keyboard.get_keyboard_lang())
    else:
        text = await select_data(callback, state)
        await callback.message.edit_text(text=text, reply_markup=Keyboard.get_keyboard_al())
        await callback.answer(show_alert=False)
    await callback.answer()


async def select_data(callback: CallbackQuery, state: FSMContext):
    name = ""
    proverka = await state.get_data()
    await state.clear()
    if callback.data == "Python" or proverka[0] in ["python_quick_sort"]:
        name = "python"
        await state.set_state(StateMenu.python)
    elif callback.data == "Rust":
        name = "rust"
        await state.set_state(StateMenu.rust)
    elif callback.data == "Java":
        name = "java"
        await state.set_state(StateMenu.java)
    elif callback.data == "JavaScript":
        name = "javascript"
        await state.set_state(StateMenu.javascript)
    elif callback.data == "C++":
        name = "c++"
        await state.set_state(StateMenu.c_plus_plus)
    else:
        print("Ошибка")

    try:
        async with aiosqlite.connect("../bot.db") as db:
            select = f"SELECT caption FROM text WHERE name=='{name}'"
            async with db.execute(select) as cursor:
                result = await cursor.fetchone()
                print(result)
                return result[0]
    except aiosqlite.Error:
        return "Ошибка"


@_router.callback_query(F.data.in_(["Python", "Rust", "C++", "JavaScript", "Java"]))
async def send_message(callback: CallbackQuery, state: FSMContext):
    text = await select_data(callback, state)
    await callback.message.edit_text(text=text, reply_markup=Keyboard.get_keyboard_al())
    await callback.answer(show_alert=False)


async def text_for_al(name):
    async with aiosqlite.connect("../bot.db") as db:
        quick_sort_text = ""
        quick_sort_code = ""
        async with db.execute(f"Select caption, code FROM text WHERE name == '{name}'") as cursor:
            result = await cursor.fetchone()
            quick_sort_text = result[0]
            quick_sort_code = result[1]
    return quick_sort_text + Pre(quick_sort_code).as_html()


@_router.callback_query(F.data == "quick_sort")
async def quick_sort_al(callback: CallbackQuery, state: FSMContext):
    data = await state.get_state()
    data = data.replace("StateMenu:", "")
    name = data + "_" + callback.data
    await state.set_data([name])
    text = await text_for_al(name)
    await callback.message.edit_text(text=text, reply_markup=Keyboard.get_keyboard_al())
    await callback.answer(show_alert=False)


@_router.callback_query(F.data == "binary_search")
async def binary_search_al(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text="binary_search", reply_markup=Keyboard.get_keyboard_al())
    await callback.answer(show_alert=False)


@_router.callback_query(F.data == "bubble_sort")
async def bubble_sort_al(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text="bubble_sort", reply_markup=Keyboard.get_keyboard_al())
    await callback.answer(show_alert=False)


@_router.callback_query(F.data == "dijkstra")
async def dijkstra_al(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text="dijkstra", reply_markup=Keyboard.get_keyboard_al())
    await callback.answer(show_alert=False)


@_router.callback_query(F.data == "DFS")
async def dfs_al(callback: CallbackQuery):
    await callback.message.edit_text(text="DFS", reply_markup=Keyboard.get_keyboard_al())
    await callback.answer(show_alert=False)