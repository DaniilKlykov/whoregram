from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import WhoreViewSet, OwnerViewSet, LightWhoreViewSet

router = DefaultRouter()
router.register(r'whores', WhoreViewSet)
router.register('owners', OwnerViewSet)
router.register(r'my-whores', LightWhoreViewSet)

urlpatterns = [
    path('', include(router.urls))
]
