from rest_framework.routers import DefaultRouter
from django.urls import path, include

from app_habits.apps import HabbitsConfig
from app_habits.views import HabitViewSet

app_name = HabbitsConfig.name

router = DefaultRouter()
router.register('habits', HabitViewSet, basename='habits')

urlpatterns = [

] + router.urls