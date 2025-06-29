# 🧠 Habit Tracker (Django + Telegram + Celery)

Этот проект — это трекер полезных привычек с возможностью получать напоминания в Telegram.

## 📌 Функциональность

- Регистрация и аутентификация пользователей (JWT)
- Создание и отслеживание привычек
- Telegram-бот с командой `/start` для активации напоминаний
- Отправка напоминаний через Celery
- Периодический опрос Telegram через Celery Beat
- Документация API через Swagger и Spectacular

---

## 🚀 Стек технологий

- Python 3.12
- Django 5
- PostgreSQL
- Redis
- Celery
- Django REST Framework
- Telegram Bot API
- Django-Celery-Beat
- Poetry

---

## 🔧 Установка и запуск

### 1. Клонируй репозиторий:

```bash
git clone https://github.com/yourname/habit-tracker.git
cd habit-tracker
```

### 2. Установи зависимости через Poetry

```bash
poetry install
```

### 3. Создай `.env` файл

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
POSTGRES_KEY=your_db_password
REDIS_URL=redis://localhost:6379
TELEGRAM_BOT_TOKEN=your_telegram_token
```

### 4. Примени миграции

```bash
poetry run python manage.py migrate
```

### 5. Запусти сервер

```bash
poetry run python manage.py runserver
```

---

## ⚙️ Celery и Beat

### Запуск Celery worker

```bash
poetry run celery -A config worker -l info
```

### Запуск Celery Beat

```bash
poetry run celery -A config beat -l info
```

---

## 📲 Telegram бот

- Найди своего бота по имени в Telegram.
- Напиши `/start`, чтобы активировать напоминания.
- Бот сохранит `chat_id`, если ты зарегистрирован с тем же `tg_username`.

---

## 🔁 Планировщик задач

Для запуска периодической отправки напоминаний:

```bash
poetry run python manage.py schedule_reminders
```

Для теста получения сообщений вручную:

```bash
poetry run python manage.py poll_telegram
```

---

## 🧪 Тестирование

```bash
poetry run pytest
```

## 📄 Лицензия

MIT License