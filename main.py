import asyncio
import logging
from aiogram import Bot, Dispatcher
from handlers import _router
from aiogram.enums import ParseMode
from Settings import config
from aiosqlite import connect


async def main():
    bot = Bot(token=config.bot_token.get_secret_value(), parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_routers(_router)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())