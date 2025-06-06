"""
handlers.py

Модуль с обработчиками команд и нажатий на кнопки.
"""

from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from keyboards import keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    """
    Обработка команды /start. Показывает меню с кнопками "Привет" и "Пока".
    """
    await message.answer(
        f"Привет, {message.from_user.first_name}! Выбери действие:",
        reply_markup=kb.get_main_reply_keyboard()
    )

@router.message(F.text == "Привет")
async def greet_user(message: Message):
    """
    Обработка кнопки "Привет".
    """
    await message.answer(f"Привет, {message.from_user.first_name}!")

@router.message(F.text == "Пока")
async def farewell_user(message: Message):
    """
    Обработка кнопки "Пока".
    """
    await message.answer(f"До свидания, {message.from_user.first_name}!")

@router.message(Command("links"))
async def cmd_links(message: Message):
    """
    Обработка команды /links. Показывает инлайн-кнопки с URL-ссылками.
    """
    await message.answer(
        "Выберите ссылку:",
        reply_markup=kb.get_links_inline_keyboard()
    )

@router.message(Command("dynamic"))
async def cmd_dynamic(message: Message):
    """
    Обработка команды /dynamic. Показывает инлайн-кнопку "Показать больше".
    """
    await message.answer(
        "Динамическое меню:",
        reply_markup=kb.get_dynamic_inline_keyboard()
    )

@router.callback_query(F.data == "show_more")
async def show_more_options(callback: CallbackQuery):
    """
    Обработка нажатия на "Показать больше" — замена клавиатуры на две опции.
    """
    await callback.message.edit_reply_markup(reply_markup=kb.get_options_inline_keyboard())
    await callback.answer()

@router.callback_query(F.data == "option_1")
async def option_1_selected(callback: CallbackQuery):
    """
    Обработка выбора "Опция 1".
    """
    await callback.message.answer("Вы выбрали: Опция 1")
    await callback.answer()

@router.callback_query(F.data == "option_2")
async def option_2_selected(callback: CallbackQuery):
    """
    Обработка выбора "Опция 2".
    """
    await callback.message.answer("Вы выбрали: Опция 2")
    await callback.answer()
