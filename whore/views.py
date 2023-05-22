from rest_framework import viewsets, filters
# from rest_framework.pagination import LimitOffsetPagination

from .permissions import OwnerOrReadOnly
from .paginations import WhorePagination

from .serializers import WhoreSerializer, AchievementSerializer
from .models import Whore, Achievement
from django_filters.rest_framework import DjangoFilterBackend


class WhoreViewSet(viewsets.ModelViewSet):
    queryset = Whore.objects.all()
    serializer_class = WhoreSerializer
    permission_classes = (OwnerOrReadOnly,)
    pagination_class = WhorePagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    pagination_class = None
    filterset_fields = ('panty_color', 'birth_year')
    search_fields = ('name', 'owner__username')
    ordering_fields = ('name', 'birth_year')
    ordering = ('birth_year')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer


# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
