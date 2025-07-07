FROM python:3.13-slim

WORKDIR /app

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y curl build-essential && rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Добавляем poetry в PATH
ENV PATH="/root/.local/bin:$PATH"

# Копируем файлы для установки зависимостей
COPY pyproject.toml poetry.lock* /app/

# Отключаем создание виртуального окружения в Poetry
RUN poetry config virtualenvs.create false

# Устанавливаем зависимости (только зависимости, не сам проект)
RUN poetry install --no-interaction --no-ansi --no-root

# Копируем весь проект в контейнер
COPY . /app/

# Запуск gunicorn напрямую без poetry run
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]