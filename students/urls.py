"""URL configuration for the students app."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"students", views.StudentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]