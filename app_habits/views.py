from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Habit
from .serializers import HabitSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response

class HabitPagination(PageNumberPagination):
    """
    Пагинация с размером страницы 5.
    """
    page_size = 5


class HabitViewSet(viewsets.ModelViewSet):
    """
    ViewSet для CRUD привычек.

    - Личные привычки доступны только авторизованному пользователю.
    - Публичные привычки доступны всем без права изменения.
    """
    serializer_class = HabitSerializer
    pagination_class = HabitPagination

    def get_permissions(self):
        if self.action == 'list_public':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        """
        Возвращает привычки текущего пользователя, либо публичные (если action list_public).
        """
        if self.action == 'list_public':
            return Habit.objects.filter(is_public=True)
        return Habit.objects.filter(user=self.request.user)

    @action(detail=False, methods=['get'], url_path='public')
    def list_public(self, request):
        """
        Список публичных привычек, доступен всем.
        """
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)