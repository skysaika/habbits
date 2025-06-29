from rest_framework import serializers
from .models import Habit

class HabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор для привычек.
    Валидирует бизнес-логику через clean() модели.
    """
    class Meta:
        model = Habit
        fields = 'all'
        read_only_fields = ('user',)

    def validate(self, data):
        """
        Вызов clean() модели для валидации.
        """
        instance = Habit(**data)
        instance.clean()
        return data