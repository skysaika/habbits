import time
import requests
import logging
from django.conf import settings
from app_users.models import User
from app_notifications.utils import API_URL, send_telegram_message

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

last_update_id = None

def get_updates():
    global last_update_id

    logger.info("Запуск Telegram polling...")

    while True:
        try:
            params = {"offset": last_update_id + 1} if last_update_id else {}
            response = requests.get(f"{API_URL}/getUpdates", params=params, timeout=10)

            if response.status_code != 200:
                logger.error("Ошибка получения обновлений от Telegram")
                time.sleep(3)
                continue

            updates = response.json().get("result", [])
            for update in updates:
                update_id = update["update_id"]
                last_update_id = update_id

                message = update.get("message")
                if not message:
                    continue

                chat = message.get("chat")
                if not chat:
                    continue

                tg_username = chat.get("username")
                chat_id = chat.get("id")
                text = message.get("text", "")

                logger.info(f"Получен chat_id: {chat_id}, username: {tg_username}, message: {text}")

                if tg_username and chat_id:
                    try:
                        user = User.objects.get(tg_username=tg_username)
                        user.tg_chat_id = chat_id
                        user.save()
                        logger.info(f"Обновлён tg_chat_id пользователя {user.email}")
                    except User.DoesNotExist:
                        logger.warning(f"Пользователь с tg_username={tg_username} не найден")

                # Ответить на команду /start
                if text.strip() == "/start":
                    send_telegram_message(chat_id, "Привет! Ты активировал бота для трекера привычек.")

        except Exception as e:
            logger.exception(f"Ошибка в get_updates: {e}")

        time.sleep(2)  # небольшая пауза между итерациями