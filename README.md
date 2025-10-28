🧩 Парсер объявлений о долгосрочной аренде квартир с Kufar с уведомлениями в Telegram

parser_kuf — это Python-скрипт для автоматического парсинга объявлений с сайта Kufar.by.
Он регулярно проверяет появление новых публикаций и отправляет уведомления в Telegram, когда находит свежие объявления.

🚀 Возможности

• 🔍 Парсинг объявлений с Kufar

• 💾 Сохранение данных в локальную базу (db.py)

• 🤖 Отправка уведомлений в Telegram-бота

• ⚙️ Настройка через .env

• 🪶 Минимум зависимостей — просто и надёжно

🛠️ Установка и запуск

1. Клонируйте репозиторий

`git clone https://github.com/Mazavinka/parser_kufar.git`

`cd parser_kufar`

2. Создайте виртуальное окружение и установите зависимости

`python -m venv venv`

`source venv/bin/activate        # для Linux/macOS`

`venv\Scripts\activate           # для Windows`

`pip install -r reqs/requirements.txt`


3. Настройте переменные окружения

Скопируйте пример файла .env.example и создайте свой .env:

`cp .env.example .env`

Откройте .env и заполните:

TG_BOT_TOKEN = your telegram bot-token

CHAT_ID = your chat id

DB_PATH = path to sqlite3 db

STARTING_URL = starting page for parsing begin

BASE_URL = base kuf url

4. Запустите парсер

`python main.py`

⚡ Технические детали

Язык: Python 3.12

Платформа: Linux / Windows / macOS

Интеграции: Telegram Bot API

Хранение: SQLite

✅ Планы развития

• Добавить логирование (logging)

• Расширить фильтры поиска (категории, ключевые слова, цена)

• Добавить тесты (pytest)

• Реализовать Dockerfile и автозапуск через GitHub Actions

🧑‍💻 Автор

📫 Telegram: @mazavinka




