from django.core.management.base import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json

class Command(BaseCommand):
    help = "Schedule Telegram polling task"

    def handle(self, *args, **kwargs):
        schedule, _ = IntervalSchedule.objects.get_or_create(
            every=30,
            period=IntervalSchedule.SECONDS,
        )

        PeriodicTask.objects.update_or_create(
            name="Poll Telegram updates",
            defaults={
                "task": "app_notifications.tasks.poll_telegram_updates",
                "interval": schedule,
                "args": json.dumps([]),
            },
        )

        self.stdout.write(self.style.SUCCESS("Задача опроса Telegram запланирована."))