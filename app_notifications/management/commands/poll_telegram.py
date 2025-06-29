from django.core.management.base import BaseCommand
from app_notifications.telegram_polling import get_updates

class Command(BaseCommand):
    help = "Poll Telegram for new updates"

    def handle(self, *args, **kwargs):
        get_updates()
        self.stdout.write(self.style.SUCCESS("Polling completed."))