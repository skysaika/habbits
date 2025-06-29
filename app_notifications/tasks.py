from celery import shared_task
from app_notifications.utils import send_telegram_message as utils_send_telegram_message

@shared_task
def send_telegram_message_task(chat_id, text):
    return utils_send_telegram_message(chat_id, text)