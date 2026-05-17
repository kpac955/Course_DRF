from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from habits.models import Habit
from habits.serializers import HabitSerializer, HabitPagination, UserRegisterSerializer
from habits.permissions import IsOwnerOrReadOnly

class UserRegisterView(generics.CreateAPIView):
    """Эндпоинт для регистрации нового пользователя"""
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

class HabitViewSet(viewsets.ModelViewSet):
    """
    Эндпоинты для работы с привычками текущего пользователя (CRUD).
    """
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        # Авторизованный пользователь видит только свои привычки
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Привязываем новой привычки к текущему пользователю
        serializer.save(user=self.request.user)


class PublicHabitListView(generics.ListAPIView):
    """
    Эндпоинт для просмотра списка публичных привычек.
    """
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = [IsAuthenticated]