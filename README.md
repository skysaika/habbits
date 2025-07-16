📈 Habit Tracker (Django + Telegram + Celery)
Трекер полезных привычек с напоминаниями через Telegram и периодическими задачами на Celery.

📌 Функциональность
- Регистрация и аутентификация пользователей (JWT)
- Создание и отслеживание привычек
- Интеграция с Telegram-ботом (/start для активации)
- Асинхронная отправка напоминаний через Celery
- Планировщик задач (Celery Beat)
- Документация API (Swagger + DRF Spectacular)

🚀 Стек технологий
- Python 3.13
- Django 5
- PostgreSQL
- Redis
- Celery & Celery Beat
- Django REST Framework
- Telegram Bot API
- Poetry (для управления зависимостями)

🔧 Установка и запуск (локально)  

1. Клонировать репозиторий:
git clone git@github.com:skysaika/habbits.git
cd habbits

2. Создать файл .env (пример — .env.example):
SECRET_KEY=ваш-секретный-ключ
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost,0.0.0.0
POSTGRES_DB=имя_базы_данных
POSTGRES_USER=пользователь_базы
POSTGRES_PASSWORD=пароль_базы
REDIS_URL=redis://localhost:6379
TELEGRAM_BOT_TOKEN=токен_вашего_бота

3. Установить зависимости:
poetry install

4. Применить миграции:
poetry run python manage.py migrate

5. Запустить сервер:
poetry run python manage.py runserver


🐳 Запуск через Docker Compose
1.Собрать и запустить контейнеры:
sudo docker compose build --no-cache
sudo docker compose up -d

2.Просмотреть логи веб-сервиса:
sudo docker compose logs -f web

3.Перейти по адресу:
http://localhost:8000

4.Остановить и удалить контейнеры и тома:
sudo docker compose down -v


⚙️ Celery и Celery Beat (вручную)

- Запуск Celery worker:
poetry run celery -A config worker -l info

- Запуск Celery Beat:
poetry run celery -A config beat -l info

⚠️ При запуске через Docker контейнеры celery и celery-beat стартуют автоматически.

📲 Использование Telegram-бота
1. Найдите вашего бота по имени в Telegram
2. Отправьте команду /start
3. Бот сохранит ваш chat_id, если ваш Telegram username совпадает с зарегистрированным в системе

⏰ Периодические задачи

- Планировщик напоминаний:
poetry run python manage.py schedule_reminders

- Опрос Telegram (вручную):
poetry run python manage.py poll_telegram

🧪 Тестирование
poetry run pytest

📄 Лицензия
Проект распространяется под лицензией MIT.