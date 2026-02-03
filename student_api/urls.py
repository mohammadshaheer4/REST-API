"""URL configuration for the student_api project."""

from django.urls import include, path

from students.views import healthcheck

urlpatterns = [
    path("api/v1/", include("students.urls")),
    path("healthcheck", healthcheck),
]
