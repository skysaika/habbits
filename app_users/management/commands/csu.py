from django.core.management.base import BaseCommand
from dotenv import load_dotenv
import os

from app_users.models import User

load_dotenv()

class Command(BaseCommand):
    help = "Создать нового суперпользователя"

    def handle(self, *args, **options):
        email = 'admin@sky.pro'
        password = os.getenv("SUPERUSER_PASSWORD")

        if not password:
            self.stdout.write(self.style.ERROR("Переменная окружения SUPERUSER_PASSWORD не установлена"))
            return

        try:
            user = User.objects.get(email=email)
            user.delete()
            self.stdout.write(self.style.SUCCESS(f"Суперпользователь с email {email} успешно удален"))
        except User.DoesNotExist:
            self.stdout.write(self.style.WARNING(f"Суперпользователь с email {email} не найден"))

        try:
            User.objects.create_superuser(
                email=email,
                password=password,
                first_name='Admin',
                last_name='SkyPro',
            )
            self.stdout.write(self.style.SUCCESS(f"Новый суперпользователь с email {email} успешно создан"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Ошибка при создании суперпользователя: {e}"))
