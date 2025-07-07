🧠 Habit Tracker (Django + Telegram + Celery)
Этот проект — трекер полезных привычек с возможностью получать напоминания через Telegram.

📌 Функциональность
Регистрация и аутентификация пользователей (JWT)

Создание и отслеживание привычек

Telegram-бот с командой /start для активации напоминаний

Отправка напоминаний асинхронно через Celery

Периодический опрос Telegram через Celery Beat

Документация API через Swagger и DRF Spectacular

🚀 Стек технологий
Python 3.13

Django 5

PostgreSQL

Redis

Celery и Celery Beat

Django REST Framework

Telegram Bot API

Poetry для управления зависимостями

🔧 Установка и запуск

1. Клонировать репозиторий(указан путь для ключа SSH)
git clone git@github.com:skysaika/habbits.git
cd habbits

2. Создать файл .env(пример в .env.example)
В корне проекта создайте файл .env и укажите необходимые переменные окружения (значения заменить на свои):
SECRET_KEY=ваш-секретный-ключ
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost,0.0.0.0,0.0.0.0:8000
POSTGRES_DB=имя_базы_данных
POSTGRES_USER=пользователь_базы
POSTGRES_PASSWORD=пароль_базы
REDIS_URL=redis://localhost:6379
TELEGRAM_BOT_TOKEN=токен_вашего_бота

3. Установить зависимости через Poetry:
    poetry install

4. Применить миграции базы данных
poetry run python manage.py migrate 

5. Запустить локально сервер разработки
poetry run python manage.py runserver

🐳 Запуск через Docker Compose
1. Собрать и запустить контейнеры
sudo docker compose build --no-cache
sudo docker compose up -d
2. Просмотреть логи веб-сервиса
sudo docker compose logs -f web
3. Перейти в браузере по адресу http://localhost:8000
4. Остановить и удалить контейнеры и тома:
sudo docker-compose down -v
⚙️ Celery и Celery Beat
Запуск Celery worker
poetry run celery -A config worker -l info
Запуск Celery Beat
poetry run celery -A config beat -l info
📲 Использование Telegram бота
Найдите вашего бота по имени в Telegram.

Отправьте команду /start для активации напоминаний.

Бот сохранит ваш chat_id, если ваш Telegram username совпадает с зарегистрированным в системе.

🔁 Периодические задачи
Для запуска планировщика напоминаний:
poetry run python manage.py schedule_reminders

Для ручного опроса Telegram:
poetry run python manage.py poll_telegram

🧪 Тестирование
poetry run pytest
📄 Лицензия
Проект распространяется под лицензией MIT.