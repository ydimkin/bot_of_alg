from aiogram import Router, Bot, F
from aiogram.types import Message
from keyboards import Keyboard
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from State import StateMenu
import aiosqlite
from aiogram.utils.formatting import Pre
from typing import Dict
from Settings import python_al, rust_al, java_al, c_plus_plus_al, javascript_al, language, alg

router = Router()


@router.callback_query(F.data == "Назад")
async def back(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    state.clear()
    if data == {}:
        text = "Выберите один из языков программирования для демонстрации алгортимов на выбранном языке"
        await callback.message.edit_text(text=text, reply_markup=Keyboard.get_keyboard_lang())
    else:
        text = await select_data(callback, state)
        await callback.message.edit_text(text=text, reply_markup=Keyboard.get_keyboard_al())
        await callback.answer(show_alert=False)
    await callback.answer()


@router.callback_query(F.data.in_(language))
async def send_message(callback: CallbackQuery, state: FSMContext):
    text = await select_data_callback(callback, state)
    await callback.message.edit_text(text="fsdfsdf", reply_markup=Keyboard.get_keyboard_al())
    await callback.answer(show_alert=False)


@router.callback_query(F.data == "quick_sort")
async def quick_sort_al(callback: CallbackQuery, state: FSMContext):
    data = await state.get_state()
    data = data.replace("StateMenu:", "")
    name = data + "_" + callback.data
    await state.set_data([name])
    text = await text_for_al(name)
    await callback.message.edit_text(text=text, reply_markup=Keyboard.get_keyboard_al())
    await callback.answer(show_alert=False)


@router.callback_query(F.data == "binary_search")
async def binary_search_al(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text="binary_search", reply_markup=Keyboard.get_keyboard_al())
    await callback.answer(show_alert=False)


@router.callback_query(F.data == "bubble_sort")
async def bubble_sort_al(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text="bubble_sort", reply_markup=Keyboard.get_keyboard_al())
    await callback.answer(show_alert=False)


@router.callback_query(F.data == "dijkstra")
async def dijkstra_al(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text="dijkstra", reply_markup=Keyboard.get_keyboard_al())
    await callback.answer(show_alert=False)


@router.callback_query(F.data == "DFS")
async def dfs_al(callback: CallbackQuery):
    await callback.message.edit_text(text="DFS", reply_markup=Keyboard.get_keyboard_al())
    await callback.answer(show_alert=False)


async def select_data_callback(callback: CallbackQuery, state: FSMContext):
    name:str
    # proverka = await state.get_data()
    # await state.clear()
    if callback.data == "Python":
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
    await select_data_bd(callback, name)


async def select_data(callback: CallbackQuery, state: FSMContext):
    name = ""
    proverka = await state.get_data()
    await state.set_data({})
    if proverka in python_al:
        name = "python"
    elif proverka in rust_al:
        name = "rust"
    elif proverka in java_al:
        name = "java"
    elif proverka in javascript_al:
        name = "javascript"
    elif proverka in c_plus_plus_al:
        name = "c++"
    return await select_data_bd(callback, name)


async def text_for_al(name):
    async with aiosqlite.connect("../bot.db") as db:
        quick_sort_text: str
        quick_sort_code: str
        async with db.execute(f"Select caption, code FROM text WHERE name == '{name}'") as cursor:
            result = await cursor.fetchone()
            quick_sort_text = result[0]
            quick_sort_code = result[1]
    return quick_sort_text + Pre(quick_sort_code).as_html()


async def select_data_bd(callback: CallbackQuery, name):
    try:
        async with aiosqlite.connect("../bot.db") as db:
            select = f"SELECT caption FROM text WHERE name=='{name}'"
            async with db.execute(select) as cursor:
                result = await cursor.fetchone()
                print(result[0])
                return result[0]
    except aiosqlite.Error:
        await callback.answer(text="Не могу подключиться к базе данных")
