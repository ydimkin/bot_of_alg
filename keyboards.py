from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import aiosqlite

class Keyboard(object):

    _key_menu_lang = [
        [
            InlineKeyboardButton(text='Python', callback_data="Python"),
            InlineKeyboardButton(text='C++', callback_data="C++")
        ],
        [
            InlineKeyboardButton(text="Rust", callback_data="Rust"),
            InlineKeyboardButton(text='JavaScript', callback_data="JavaScript")

        ],
        [
            InlineKeyboardButton(text='Java', callback_data="Java"),
        ],
        [
            InlineKeyboardButton(text="Редактировать", callback_data="edit")
        ]
    ]
    _key_menu_al = [
        [
            InlineKeyboardButton(text="Быстрая сортировка", callback_data="quick_sort"),
            InlineKeyboardButton(text="Бинарный поиск", callback_data="binary_search")
        ],
        [
            InlineKeyboardButton(text="Cортировки пузырьком", callback_data="bubble_sort"),
            InlineKeyboardButton(text="Дейкстры", callback_data="dijkstra")
        ],
        [
            InlineKeyboardButton(text="Поиск в глубину", callback_data="DFS"),
        ],
        [
            InlineKeyboardButton(text="Назад ↩", callback_data="Назад"),
        ],
        [
            InlineKeyboardButton(text="Редактировать", callback_data="edit")
        ]
    ]
    _key_menu_al1 = [
        [
            InlineKeyboardButton(text="Назад ↩", callback_data="Назад")
        ],
        [
            InlineKeyboardButton(text="Редактировать", callback_data="edit")
        ]
    ]

    @classmethod
    def get_keyboard_lang(cls) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(inline_keyboard=cls._key_menu_lang)

    @classmethod
    def get_keyboard_al(cls) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(inline_keyboard=cls._key_menu_al)

    # async def check_admin(self):
    #     async with aiosqlite.connect("bot.db") as db:



    @classmethod
    def get_keyboard_al1(cls) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(inline_keyboard=cls._key_menu_al1)
