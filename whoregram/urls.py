from rest_framework import routers
from rest_framework import permissions

from django.contrib import admin
from django.urls import include, path #  re_path

from django.conf import settings
from django.conf.urls.static import static

from whore.views import AchievementViewSet, WhoreViewSet

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = routers.DefaultRouter()
router.register(r'whores', WhoreViewSet)
router.register(r'achievements', AchievementViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Whore API",
      default_version='v1',
      description="Проект 'Шлюхограм'",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.authtoken')),
    # re_path(r'^swagger(?P\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
