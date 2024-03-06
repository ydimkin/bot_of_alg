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
import html

router = Router()


@router.callback_query(F.data == "Назад")
async def back(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
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
    await callback.message.edit_text(text=text, reply_markup=Keyboard.get_keyboard_al())
    await callback.answer(show_alert=False)


async def al_text(callback: CallbackQuery, state: FSMContext):
    data = await state.get_state()
    data = data.replace("StateMenu:", "")
    name = data + "_" + callback.data
    await state.set_data([name])
    return await text_for_al(name)


@router.callback_query(F.data == "quick_sort")
async def quick_sort_al(callback: CallbackQuery, state: FSMContext):
    text = await al_text(callback, state)
    await callback.message.edit_text(text=text, reply_markup=Keyboard.get_keyboard_al1())
    await callback.answer(show_alert=False)


@router.callback_query(F.data == "binary_search")
async def binary_search_al(callback: CallbackQuery, state: FSMContext):
    text = await al_text(callback, state)
    await callback.message.edit_text(text=text, reply_markup=Keyboard.get_keyboard_al1())
    await callback.answer(show_alert=False)


@router.callback_query(F.data == "bubble_sort")
async def bubble_sort_al(callback: CallbackQuery, state: FSMContext):
    text = await al_text(callback, state)
    await callback.message.edit_text(text=text, reply_markup=Keyboard.get_keyboard_al1())
    await callback.answer(show_alert=False)


@router.callback_query(F.data == "dijkstra")
async def dijkstra_al(callback: CallbackQuery, state: FSMContext):
    text = await al_text(callback, state)
    await callback.message.edit_text(text=text, reply_markup=Keyboard.get_keyboard_al1())
    await callback.answer(show_alert=False)


@router.callback_query(F.data == "DFS")
async def dfs_al(callback: CallbackQuery, state: FSMContext):
    text = await al_text(callback, state)
    await callback.message.edit_text(text=text, reply_markup=Keyboard.get_keyboard_al1())
    await callback.answer(show_alert=False)


async def select_data_callback(callback: CallbackQuery, state: FSMContext):
    name: str
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
        name = "c"
        await state.set_state(StateMenu.c)
    return await select_data_bd(callback, name)


async def select_data(callback: CallbackQuery, state: FSMContext):
    name = ""
    proverka = await state.get_data()
    await state.set_data({})
    if proverka[0] in python_al:
        name = "python"
    elif proverka[0] in rust_al:
        name = "rust"
    elif proverka[0] in java_al:
        name = "java"
    elif proverka[0] in javascript_al:
        name = "javascript"
    elif proverka[0] in c_plus_plus_al:
        name = "c"
    return await select_data_bd(callback, name)


async def text_for_al(name):
    async with aiosqlite.connect("bot.db") as db:
        text: str
        code: str
        async with db.execute(f"Select caption, code FROM text WHERE name == '{name}'") as cursor:
            result = await cursor.fetchone()
            text = result[0]
            code = result[1]
    return text + Pre(code).as_html()


async def select_data_bd(callback: CallbackQuery, name):
    try:
        async with aiosqlite.connect("bot.db") as db:
            select = f"SELECT caption FROM text WHERE name=='{name}'"
            async with db.execute(select) as cursor:
                result = await cursor.fetchone()
                return result[0]
    except aiosqlite.Error:
        await callback.answer(text="Не могу подключиться к базе данных")
