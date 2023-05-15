from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import WhoreViewSet, OwnerViewSet

router = DefaultRouter()
router.register('whores', WhoreViewSet)
router.register('owners', OwnerViewSet)

urlpatterns = [
    path('', include(router.urls))
]
