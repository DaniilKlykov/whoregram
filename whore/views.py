from rest_framework import viewsets

from .serializers import WhoreSerializer, UserSerializer, AchievementSerializer
from .models import Whore, Achievement, User


class WhoreViewSet(viewsets.ModelViewSet):
    queryset = Whore.objects.all()
    serializer_class = WhoreSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
