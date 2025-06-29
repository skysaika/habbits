from celery import shared_task
from app_notifications.telegram_polling import poll_telegram_updates
from app_notifications.utils import send_telegram_message
from app_users.models import User

@shared_task
def send_telegram_message_task(chat_id, text):
    return send_telegram_message(chat_id, text)

@shared_task
def send_reminders():
    users = User.objects.exclude(tg_chat_id__isnull=True)
    for user in users:
        send_telegram_message(user.tg_chat_id, "⏰ Напоминание: не забудь выполнить полезную привычку сегодня!")

@shared_task(name="app_notifications.tasks.poll_telegram_updates")
def poll_telegram_updates_task():
    poll_telegram_updates()