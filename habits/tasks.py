import requests
from celery import shared_task
from django.conf import settings

from habits.models import Habit


@shared_task
def send_telegram_notification(habit_id):
    try:
        habit = Habit.objects.get(pk=habit_id)

        token = settings.TELEGRAM_BOT_TOKEN
        chat_id = settings.TELEGRAM_CHAT_ID

        message = (
            f"⏰ ПОРА ДЕЙСТВОВАТЬ!\n\n"
            f"Привычка: {habit.action}\n"
            f"Место: {habit.place}\n"
            f"Время: {habit.time}"
        )

        url = f"https://api.telegram.org/bot{token}/sendMessage"
        response = requests.post(url, data={"chat_id": chat_id, "text": message})

        return response.json()
    except Habit.DoesNotExist:
        return f"Привычка {habit_id} не найдена."
