from rest_framework import status
from rest_framework.test import APITestCase

class HabitTestCase(APITestCase):
    def test_habit_list(self):
        """ Тестируем, что эндпоинт привычек доступен """
        response = self.client.get('/habits/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)