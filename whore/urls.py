from django.urls import path

from .views import whore_list, whore_detail, WhoreListApi

urlpatterns = [
    path('whores/', WhoreListApi.as_view()),
    path('whores/<int:pk>/', whore_detail),
]
