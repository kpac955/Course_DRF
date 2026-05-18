from rest_framework import status
from rest_framework.test import APITestCase

class HabitTestCase(APITestCase):
    def test_docs_available(self):
        """ Проверяем доступность документации Swagger """
        response = self.client.get('/api/docs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habits_list_endpoint(self):
        """ Проверяем эндпоинт привычек 1 """
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)