from rest_framework import serializers
from .models import Habit

class HabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор для привычек.
    Валидирует бизнес-логику через clean() модели.
    """
    class Meta:
        model = Habit
        fields = '__all__'
        read_only_fields = ('user',)

    def validate(self, data):
        """
        Вызов clean() модели для валидации.
        """
        instance = Habit(**data)
        instance.clean()
        return data

    def create(self, validated_data):
        """
        Автоматически добавляем пользователя из контекста запроса.
        """
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)