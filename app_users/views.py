from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated

from app_users.models import User
from app_users.serializers import RegisterSerializer, UserProfileSerializer

class RegisterView(generics.CreateAPIView):
    """
    Вью для регистрации нового пользователя.
    Доступна без авторизации.
    """
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

class UserProfileView(generics.RetrieveUpdateAPIView):
    """
    Вью для просмотра и редактирования профиля текущего пользователя.
    Требуется авторизация.
    """
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """
        Возвращает объект текущего пользователя.
        """
        return self.request.user