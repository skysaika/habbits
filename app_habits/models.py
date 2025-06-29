from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

class Habit(models.Model):
    """
    Модель полезной или приятной привычки.

    Поля:
    - user: создатель привычки
    - place: место выполнения
    - time: время выполнения
    - action: описание действия
    - is_pleasant: булево, признак приятной привычки
    - related_habit: связь с приятной привычкой (если это полезная)
    - periodicity: периодичность в днях (минимум 7)
    - reward: вознаграждение после выполнения
    - duration_seconds: время выполнения (максимум 120 секунд)
    - is_public: признак публичности привычки
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='habits')
    place = models.CharField(max_length=255, verbose_name="Место")
    time = models.TimeField(verbose_name="Время")
    action = models.CharField(max_length=255, verbose_name="Действие")
    is_pleasant = models.BooleanField(default=False, verbose_name="Приятная привычка")
    related_habit = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL,
                                      limit_choices_to={'is_pleasant': True},
                                      verbose_name="Связанная привычка")
    periodicity = models.PositiveIntegerField(default=1, verbose_name="Периодичность (дни)", help_text="Минимум 7 дней")
    reward = models.CharField(max_length=255, null=True, blank=True, verbose_name="Вознаграждение")
    duration_seconds = models.PositiveIntegerField(verbose_name="Время выполнения (секунды)")
    is_public = models.BooleanField(default=False, verbose_name="Публичная")

    def clean(self):
        """
        Валидация модели:
        - нельзя одновременно указывать related_habit и reward
        - время выполнения <= 120 секунд
        - периодичность >= 7 дней
        - у приятной привычки не может быть related_habit или reward
        """
        errors = {}

        if self.related_habit and self.reward:
            errors['reward'] = 'Нельзя одновременно указывать связанную привычку и вознаграждение.'
            errors['related_habit'] = 'Нельзя одновременно указывать связанную привычку и вознаграждение.'

        if self.duration_seconds > 120:
            errors['duration_seconds'] = 'Время выполнения не может превышать 120 секунд.'

        if self.periodicity < 7:
            errors['periodicity'] = 'Периодичность должна быть не меньше 7 дней.'

        if self.is_pleasant:
            if self.reward:
                errors['reward'] = 'У приятной привычки не может быть вознаграждения.'
            if self.related_habit:
                errors['related_habit'] = 'У приятной привычки не может быть связанной привычки.'

        if errors:
            raise ValidationError(errors)

    def __str__(self):
        return f"{self.action} в {self.time} @ {self.place}"

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
        ordering = ['time']
