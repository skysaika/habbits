from django.core.management.base import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        schedule, _ = IntervalSchedule.objects.get_or_create(
            every=10,
            period=IntervalSchedule.MINUTES,
        )

        PeriodicTask.objects.update_or_create(
            name="Send habit reminders",
            defaults={
                "task": "app_notifications.tasks.send_reminders",
                "interval": schedule,
                "args": json.dumps([]),
            },
        )

        self.stdout.write(self.style.SUCCESS("Задача напоминания запланирована."))
        # запуск: poetry run python manage.py schedule_reminders