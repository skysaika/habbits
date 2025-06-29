from django.core.management.base import BaseCommand
from app_notifications.telegram_polling import poll_telegram_updates

class Command(BaseCommand):
    help = "Poll Telegram for new updates"

    def handle(self, *args, **kwargs):
        poll_telegram_updates()
        self.stdout.write(self.style.SUCCESS("Polling completed."))