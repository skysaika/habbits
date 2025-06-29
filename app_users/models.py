from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None  # убираем username
    email = models.EmailField(unique=True)
    tg_username = models.CharField(max_length=50, unique=True)
    tg_chat_id = models.CharField(max_length=50, unique=True, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["tg_username"]

    def str(self):
        return self.email
