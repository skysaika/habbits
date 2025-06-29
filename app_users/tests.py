from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class UserTests(APITestCase):
    def test_register_user(self):
        url = reverse('app_users:register')  # URL эндпоинта регистрации
        data = {
            'email': 'test@example.com',
            'password': 'StrongPass123',
            'password2': 'StrongPass123',
            'first_name': 'Test',
            'last_name': 'User'
        }
        response = self.client.post(url, data)  # Отправляем POST-запрос на регистрацию
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Проверяем успешный ответ
        self.assertTrue(User.objects.filter(email='test@example.com').exists())  # Проверяем, что пользователь создан

    def test_profile_retrieve_update(self):
        # Создаем пользователя напрямую через ORM
        user = User.objects.create_user(email='user@example.com', password='pass1234')
        # Принудительно аутентифицируемся в тестовом клиенте
        self.client.force_authenticate(user=user)
        url = reverse('app_users:profile')  # URL эндпоинта профиля

        # Получаем профиль (GET)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], user.email)

        # Обновляем профиль (PATCH)
        data = {'first_name': 'NewName'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user.refresh_from_db()  # Обновляем объект из базы
        self.assertEqual(user.first_name, 'NewName')

