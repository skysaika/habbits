import requests
import logging
from app_users.models import User
from app_notifications.utils import API_URL, send_telegram_message
import redis

logger = logging.getLogger(__name__)

redis_client = redis.Redis(host='localhost', port=6379, db=0)  # Укажи свои параметры, если нужны

REDIS_LAST_UPDATE_ID_KEY = "telegram:last_update_id"

def poll_telegram_updates():
    """
    Делает один запрос к Telegram API для получения обновлений.
    Хранит last_update_id в Redis.
    """
    try:
        last_update_id = redis_client.get(REDIS_LAST_UPDATE_ID_KEY)
        if last_update_id is not None:
            last_update_id = int(last_update_id)

        params = {"offset": last_update_id + 1} if last_update_id is not None else {}

        response = requests.get(f"{API_URL}/getUpdates", params=params, timeout=10)
        response.raise_for_status()

        updates = response.json().get("result", [])

        if not updates:
            logger.info("Нет новых обновлений от Telegram")
            return

        max_update_id = None

        for update in updates:
            update_id = update["update_id"]
            if max_update_id is None or update_id > max_update_id:
                max_update_id = update_id

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

            if text.strip() == "/start":
                send_telegram_message(chat_id, "Привет! Ты активировал бота для трекера привычек.")

        if max_update_id is not None and max_update_id != last_update_id:
            redis_client.set(REDIS_LAST_UPDATE_ID_KEY, max_update_id)

    except requests.RequestException as e:
        logger.error(f"Ошибка HTTP запроса к Telegram API: {e}")
    except Exception as e:
        logger.exception(f"Общая ошибка в poll_telegram_updates: {e}")