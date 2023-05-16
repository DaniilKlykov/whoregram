from rest_framework import viewsets, mixins

from .serializers import WhoreSerializer, OwnerSerializer, WhoreListSerializer
from .models import Whore, Owner

from rest_framework.decorators import action
from rest_framework.response import Response


class CreateRetrieveDeleteViewSet(mixins.CreateModelMixin,
                                  mixins.DestroyModelMixin,
                                  mixins.RetrieveModelMixin,
                                  viewsets.GenericViewSet):
    pass


class LightWhoreViewSet(CreateRetrieveDeleteViewSet):
    queryset = Whore.objects.all()
    serializer_class = WhoreSerializer


class WhoreViewSet(viewsets.ModelViewSet):
    queryset = Whore.objects.all()
    serializer_class = WhoreSerializer

    @action(detail=False, url_path='recent-white-whores')
    def recent_white_whores(self, request):
        whores = Whore.objects.filter(panty_color='White').order_by(
            '-birth_year')[:5]
        serializer = self.get_serializer(whores, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'list':
            return WhoreListSerializer
        return WhoreSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
