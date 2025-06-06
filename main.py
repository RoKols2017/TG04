"""
main.py

Главная точка входа. Запуск бота, регистрация роутеров.
"""

import asyncio
from aiogram import Bot, Dispatcher

from config import TOKEN
from handlers import handlers

async def main():
    """
    Инициализация бота и запуск polling.
    """
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(handlers.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
