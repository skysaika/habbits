from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        """
        Создает и сохраняет пользователя с email и паролем.
        """
        if not email:
            raise ValueError('Email должен быть установлен')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Создает и сохраняет суперпользователя с email и паролем.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None  # убираем username
    email = models.EmailField(unique=True, verbose_name='почта')
    tg_username = models.CharField(
        max_length=50,
        unique=True,
        null=True,
        blank=True,
        verbose_name='Имя в телеграме'
    )
    tg_chat_id = models.CharField(
        max_length=50,
        unique=True,
        null=True,
        blank=True,
        verbose_name='ID в телеграме'
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # если нужны обязательные поля при создании суперпользователя, добавьте сюда

    objects = UserManager()  # подключаем кастомный менеджер

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['email']
