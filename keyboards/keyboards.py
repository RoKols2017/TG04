"""
keyboards.py

Модуль для создания клавиатур (reply и inline) для Telegram-бота на aiogram 3.x.
"""

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_main_reply_keyboard() -> ReplyKeyboardMarkup:
    """
    Главная клавиатура с кнопками "Привет" и "Пока".
    """
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Привет"), KeyboardButton(text="Пока")]
        ],
        resize_keyboard=True
    )

def get_links_inline_keyboard() -> InlineKeyboardMarkup:
    """
    Инлайн-клавиатура с тремя кнопками-ссылками.
    """
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Новости", url="https://vgtrk.ru/russia24")],
            [InlineKeyboardButton(text="Музыка", url="https://music.yandex.ru/")],
            [InlineKeyboardButton(text="Видео", url="https://www.youtube.com/")]
        ]
    )

def get_dynamic_inline_keyboard() -> InlineKeyboardMarkup:
    """
    Клавиатура с одной инлайн-кнопкой "Показать больше".
    """
    builder = InlineKeyboardBuilder()
    builder.button(text="Показать больше", callback_data="show_more")
    return builder.as_markup()

def get_options_inline_keyboard() -> InlineKeyboardMarkup:
    """
    Клавиатура с двумя опциями для динамического меню.
    """
    builder = InlineKeyboardBuilder()
    builder.button(text="Опция 1", callback_data="option_1")
    builder.button(text="Опция 2", callback_data="option_2")
    builder.adjust(2)
    return builder.as_markup()
