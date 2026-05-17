from rest_framework.exceptions import ValidationError

class HabitValidator:
    def __call__(self, attrs):
        associated_habit = attrs.get('associated_habit')
        reward = attrs.get('reward')
        is_pleasant = attrs.get('is_pleasant', False)
        periodicity = attrs.get('periodicity')

        # 1. Исключить одновременный выбор связанной привычки и вознаграждения
        if associated_habit and reward:
            raise ValidationError(
                "Нельзя одновременно заполнять 'Связанную привычку' и 'Вознаграждение'."
            )

        # 2. У приятной привычки не может быть вознаграждения или связанной привычки
        if is_pleasant:
            if associated_habit or reward:
                raise ValidationError(
                    "У приятной привычки не может быть вознаграждения или связанной привычки."
                )

        # 3. В связанные привычки могут попадать только привычки с признаком приятной
        if associated_habit and not associated_habit.is_pleasant:
            raise ValidationError(
                "Связанная привычка должна иметь признак приятной привычки (is_pleasant=True)."
            )

        # 4. Нельзя выполнять привычку реже, чем 1 раз в 7 дней
        if periodicity is not None and (periodicity < 1 or periodicity > 7):
            raise ValidationError(
                "Периодичность выполнения должна быть от 1 до 7 дней."
            )