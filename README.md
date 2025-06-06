# TG-Bot на Aiogram 3.x

Современный Telegram-бот на Python с использованием фреймворка [aiogram 3.20.0post0](https://docs.aiogram.dev/), реализующий пример интерактивного меню, кнопок и динамических инлайн-клавиатур.

## 🚀 Особенности

* Структурированный и читаемый код
* Разделение на обработчики, клавиатуры и конфиг
* Поддержка reply- и inline-клавиатур
* Динамическое обновление кнопок по нажатию
* Асинхронность и лучшие практики архитектуры aiogram

---

## 📂 Структура проекта

```
TG_Bot/
├── handlers/              # Пакет с роутерами/обработчиками (по группам логики)
│   ├── __init__.py
│   └── handlers.py
├── keyboards/             # Пакет со всеми клавиатурами (разделяй по смыслу если надо)
│   ├── __init__.py
│   └── keyboards.py
├── config.py              # Конфиг: загрузка токенов и прочих настроек
├── main.py                # Точка входа, инициализация бота и запуск
├── .env                   # Личные переменные окружения (НЕ пушить в git)
├── .env_example           # Пример .env
├── requirements.txt       # Зависимости проекта
├── README.md              # Описание и инструкция
└── img.PNG                # Картинка для примеров/README
```

---

## ⚙️ Быстрый старт

1. **Склонируйте проект:**

   ```bash
   git clone https://github.com/yourusername/TG_Bot.git
   cd TG_Bot
   ```

2. **Установите зависимости:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Создайте свой `.env` на основе шаблона:**

   ```bash
   cp .env_example .env
   ```

   Вставьте в `.env` токен вашего Telegram-бота:

   ```
   BOT_TOKEN=ваш_секретный_токен
   ```

4. **Запустите бота:**

   ```bash
   python main.py
   ```

---

## 📝 Основные команды бота

* `/start` — главное меню с reply-кнопками "Привет" и "Пока"
* `/links` — инлайн-кнопки с URL-ссылками на новости, музыку и видео
* `/dynamic` — динамическое инлайн-меню (по нажатию кнопки появляются новые опции)

---

## 🛠️ Примеры кода

### Создание Reply-клавиатуры

```python
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Привет"), KeyboardButton(text="Пока")]],
    resize_keyboard=True
)
```

### Создание Inline-клавиатуры

```python
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Россия 24", url="https://vgtrk.ru/russia24")],
        [InlineKeyboardButton(text="Музыка", url="https://music.yandex.ru/")],
        [InlineKeyboardButton(text="Видео", url="https://www.youtube.com/")]
    ]
)
```

---

## 📦 Зависимости

* Python >= 3.9
* aiogram==3.20.0post0
* python-dotenv

**Установить всё:**

```bash
pip install -r requirements.txt
```

---

## 🔒 Безопасность

* Никогда не выкладывайте свои `.env` и токены в публичный репозиторий!
* Добавьте `.env` в `.gitignore`.

---

## 🐳 Деплой

Для запуска на сервере рекомендуется использовать:

* [systemd](https://wiki.archlinux.org/title/Systemd) юнит или аналоги для process management
* [Heroku](https://heroku.com/), [Fly.io](https://fly.io/), \[Yandex Cloud] и другие PaaS-платформы.

---

## 🖼️ Скриншоты

![Картинка](https://github.com/RoKols2017/TG04/img.png)


---

## ❓ FAQ

**Q:** Бот не отвечает на команды!
**A:** Проверьте, что вы вставили правильный токен и бот запущен.

**Q:** Как добавить новую кнопку?
**A:** Добавьте кнопку в файл `keyboards.py` и создайте для неё обработчик в `handlers.py`.

**Q:** Где посмотреть логи?
**A:** Запускайте бота с помощью:

```bash
python -u main.py
```

Или подключайте логирование через модуль `logging`.

---

## 🤝 Контакты

* [Aiogram документация](https://docs.aiogram.dev/)
* [Официальный Telegram @BotFather](https://t.me/BotFather)
* Связь с автором: \[[RoKols2017@gmail.com](mailto:your-email@example.com)]

---

## Лицензия

MIT License
