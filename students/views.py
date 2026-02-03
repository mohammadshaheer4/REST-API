"""Views for the students app."""

import logging

from django.db import connection
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer

logger = logging.getLogger(__name__)


@api_view(["GET"])
@renderer_classes([JSONRenderer])
def healthcheck(request):
    """Check the health status of the API and database connection."""
    try:
        connection.ensure_connection()
        db_status = "healthy"
    except Exception:
        db_status = "unhealthy"
    return Response({"status": "ok", "database": db_status})


class StudentViewSet(viewsets.ModelViewSet):
    """ViewSet for CRUD operations on Student model."""

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def list(self, request, *args, **kwargs):
        """List all students."""
        response = super().list(request, *args, **kwargs)
        logger.info("Listed %d students", len(response.data))
        return response

    def create(self, request, *args, **kwargs):
        """Create a new student."""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Created student id=%s", serializer.data["id"])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create student: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """Update an existing student."""
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Updated student id=%s", instance.pk)
            return Response(serializer.data)
        logger.error("Failed to update student id=%s: %s", instance.pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """Delete a student."""
        instance = self.get_object()
        pk = instance.pk
        instance.delete()
        logger.info("Deleted student id=%s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)