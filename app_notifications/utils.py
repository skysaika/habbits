import requests
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

API_URL = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}"

def send_telegram_message(chat_id, text):
    url = f"{API_URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        logger.warning(f"Ошибка при отправке Telegram-сообщения в чат {chat_id}: {e}")
        # Можно вернуть None или False, если нужно
        return None