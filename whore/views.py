from rest_framework import viewsets

from .serializers import WhoreSerializer, OwnerSerializer
from .models import Whore, Owner


class WhoreViewSet(viewsets.ModelViewSet):
    queryset = Whore.objects.all()
    serializer_class = WhoreSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
