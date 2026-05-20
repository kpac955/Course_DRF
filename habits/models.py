from django.conf import settings
from django.core.validators import MaxValueValidator
from django.db import models


class Habit(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Создатель",
        related_name="habits",
    )
    place = models.CharField(max_length=255, verbose_name="Место выполнения")
    time = models.TimeField(verbose_name="Время выполнения")
    action = models.CharField(max_length=255, verbose_name="Действие")

    is_pleasant = models.BooleanField(default=False, verbose_name="Признак приятной привычки")

    associated_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Связанная привычка",
        related_name="parent_habits",
    )

    # Периодичность в днях: 1 - каждый день, 7 - раз в неделю
    periodicity = models.PositiveSmallIntegerField(default=1, verbose_name="Периодичность (в днях)")

    reward = models.CharField(max_length=255, null=True, blank=True, verbose_name="Вознаграждение")

    # Время на выполнение в секундах
    duration = models.PositiveSmallIntegerField(
        default=60,
        validators=[MaxValueValidator(120)],
        verbose_name="Время на выполнение (в секундах)",
    )

    is_public = models.BooleanField(default=False, verbose_name="Признак публичности")

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
        ordering = ["id"]

    def __str__(self):
        return f"{self.user} будет {self.action} в {self.time} в {self.place}"
