from django.contrib.auth import get_user_model
from rest_framework import serializers

from habits.models import Habit
from habits.validators import HabitValidator

User = get_user_model()


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        read_only_fields = ("user",)
        validators = [HabitValidator()]


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "password")

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data["username"], password=validated_data["password"])
        return user
