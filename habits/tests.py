import datetime

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit

User = get_user_model()


class HabitTestCase(APITestCase):

    def setUp(self):
        """Подготовка данных перед каждым тестом"""
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.other_user = User.objects.create_user(username="otheruser", password="testpassword")

        # Создаем привычки
        self.habit = Habit.objects.create(
            user=self.user,
            place="Дом",
            time=datetime.time(8, 0),
            action="Сделать зарядку",
            periodicity=1,
            duration=60,
            is_public=False,
        )

        self.public_habit = Habit.objects.create(
            user=self.other_user,
            place="Парк",
            time=datetime.time(19, 0),
            action="Пробежка",
            periodicity=1,
            duration=90,
            is_public=True,
        )

    def test_create_habit(self):
        """Тест создания привычки авторизованным пользователем"""
        self.client.force_authenticate(user=self.user)

        data = {
            "place": "Офис",
            "time": "12:00:00",
            "action": "Выпить стакан воды",
            "periodicity": 1,
            "duration": 30,
        }

        response = self.client.post(reverse("habits-list"), data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.filter(user=self.user).count(), 2)
        self.assertEqual(response.json()["action"], "Выпить стакан воды")

    def test_get_user_habits_list(self):
        """Тест: пользователь видит только свои приватные привычки во ViewSet"""
        self.client.force_authenticate(user=self.user)

        response = self.client.get(reverse("habits-list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()["results"]), 1)
        self.assertEqual(response.json()["results"][0]["action"], "Сделать зарядку")

    def test_get_public_habits_list(self):
        """Тест получения списка публичных привычек"""
        self.client.force_authenticate(user=self.user)

        response = self.client.get(reverse("public-habits"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()["results"]), 1)
        self.assertEqual(response.json()["results"][0]["action"], "Пробежка")
