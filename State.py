from aiogram.fsm.state import State, StatesGroup


class StateMenu(StatesGroup):
    python = State()
    rust = State()
    javascript = State()
    java = State()
    c = State()
    edit = State()