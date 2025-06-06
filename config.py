"""
config.py

Модуль для загрузки конфигурации бота из переменных окружения.
"""

import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
