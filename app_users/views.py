from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from app_users.serializers import RegisterSerializer, UserProfileSerializer

class RegisterView(generics.CreateAPIView):
    """
    Вью для регистрации нового пользователя.
    Доступна без авторизации.
    """
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

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