from aiogram import Router, Bot, F
from aiogram.types import Message
from keyboards import Keyboard
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from State import StateMenu
import aiosqlite
from aiogram.utils.formatting import Pre
from Settings import python_al, rust_al, java_al, c_plus_plus_al, javascript_al, language, alg, database
from .comands import send_menu

router = Router()


async def get_role(telegram_id):
    async with aiosqlite.connect(database) as bd:
        result: None
        request = f"SELECT role from Users Where telegram_id=={telegram_id}"
        async with bd.execute(request) as cursor:
            result = await cursor.fetchone()
        return result[0]

@router.callback_query(F.data == "Назад")
async def back(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    async def menu():
        await state.clear()
        text = "Выберите один из языков программирования для демонстрации алгортимов на выбранном языке"
        await callback.message.edit_text(text=text, reply_markup=Keyboard.get_keyboard_lang())

    if data == {}:
        await menu()

    elif data["name"] in ["python", "java", "rust", "javascript", "c"]:
        await menu()
    else:
        text = await select_data(callback, state)
        role = await get_role(callback.from_user.id)
        await callback.message.edit_text(text=text, reply_markup=Keyboard.get_keyboard_al(role))
        data = await state.get_data()
        index = data["name"].find("_")
        await state.set_data({'name': data["name"][:index]})
    await callback.answer()


# Обработчик выбранного языка, вывод меню с кнопками выбора алгоритмов
@router.callback_query(F.data.in_(language))
async def send_message(callback: CallbackQuery, state: FSMContext):
    text = await select_data_callback(callback, state)
    role = await get_role(callback.from_user.id)
    await callback.message.edit_text(text=text, reply_markup=Keyboard.get_keyboard_al(role))
    await callback.answer(show_alert=False)


@router.callback_query(F.data == "quick_sort")
async def quick_sort_al(callback: CallbackQuery, state: FSMContext):
    text = await al_text(callback, state)
    role = await get_role(callback.from_user.id)
    await callback.message.edit_text(text=text, reply_markup=Keyboard.get_keyboard_al1(role))
    await callback.answer(show_alert=False)


@router.callback_query(F.data == "binary_search")
async def binary_search_al(callback: CallbackQuery, state: FSMContext):
    text = await al_text(callback, state)
    role = await get_role(callback.from_user.id)
    await callback.message.edit_text(text=text, reply_markup=Keyboard.get_keyboard_al1(role))
    await callback.answer(show_alert=False)


@router.callback_query(F.data == "bubble_sort")
async def bubble_sort_al(callback: CallbackQuery, state: FSMContext):
    text = await al_text(callback, state)
    role = await get_role(callback.from_user.id)
    await callback.message.edit_text(text=text, reply_markup=Keyboard.get_keyboard_al1(role))
    await callback.answer(show_alert=False)


@router.callback_query(F.data == "dijkstra")
async def dijkstra_al(callback: CallbackQuery, state: FSMContext):
    text = await al_text(callback, state)
    role = await get_role(callback.from_user.id)
    await callback.message.edit_text(text=text, reply_markup=Keyboard.get_keyboard_al1(role))
    await callback.answer(show_alert=False)


@router.callback_query(F.data == "DFS")
async def dfs_al(callback: CallbackQuery, state: FSMContext):
    text = await al_text(callback, state)
    role = await get_role(callback.from_user.id)
    await callback.message.edit_text(text=text, reply_markup=Keyboard.get_keyboard_al1(role))
    await callback.answer(show_alert=False)


async def al_text(callback: CallbackQuery, state: FSMContext):
    data = await state.get_state()
    data = data.replace("StateMenu:", "")
    name = data + "_" + callback.data
    await state.set_data({
        "name": name
    })
    return await text_for_al(name)


async def select_data_callback(callback: CallbackQuery, state: FSMContext):
    name: str
    # proverka = await state.get_data()
    # await state.clear()
    if callback.data == "Python":
        name = "python"
        await state.set_state(StateMenu.python)
        await state.set_data({"name": name})
    elif callback.data == "Rust":
        name = "rust"
        await state.set_state(StateMenu.rust)
        await state.set_data({"name": name})
    elif callback.data == "Java":
        name = "java"
        await state.set_state(StateMenu.java)
        await state.set_data({"name": name})
    elif callback.data == "JavaScript":
        name = "javascript"
        await state.set_state(StateMenu.javascript)
        await state.set_data({"name": name})
    elif callback.data == "C++":
        name = "c"
        await state.set_state(StateMenu.c)
    return await select_data_bd(callback, name)


async def select_data(callback: CallbackQuery, state: FSMContext):
    name = ""
    proverka = await state.get_data()
    print(proverka)
    if proverka["name"] in python_al:
        name = "python"
    elif proverka["name"] in rust_al:
        name = "rust"
    elif proverka["name"] in java_al:
        name = "java"
    elif proverka["name"] in javascript_al:
        name = "javascript"
    elif proverka["name"] in c_plus_plus_al:
        name = "c"
    return await select_data_bd(callback, name)


async def text_for_al(name):
    async with aiosqlite.connect(database) as db:
        text: str
        code: str
        async with db.execute(f"Select caption, code FROM text WHERE name == '{name}'") as cursor:
            result = await cursor.fetchone()
            text = result[0]
            code = result[1]
    return text + Pre(code).as_html()


async def select_data_bd(callback: CallbackQuery, name):
    try:
        async with aiosqlite.connect(database) as db:
            select = f"SELECT caption FROM text WHERE name=='{name}'"
            async with db.execute(select) as cursor:
                result = await cursor.fetchone()
                return result[0]
    except aiosqlite.Error:
        await callback.answer(text="Не могу подключиться к базе данных")


@router.callback_query(F.data == "edit")
async def edit_text(calllback: CallbackQuery, state: FSMContext, bot: Bot):
    await state.set_state(StateMenu.edit)
    await bot.send_message(calllback.message.chat.id, text="Отправьте текст для изменения")
    await calllback.answer()

@router.message(F.text, StateMenu.edit)
async def hand_text_edit(msg: Message, bot: Bot, state: FSMContext):
    data = await state.get_data()
    print(data)
    name_table = data["name"]
    text_edit = msg.text
    async with aiosqlite.connect(database) as db:
        update_request = f"UPDATE text set caption='{text_edit}' where name='{name_table}'"
        await db.execute(update_request)
        await db.commit()
    await bot.send_message(msg.chat.id, text="Текст изменен")
    await send_menu(msg, bot, state)

