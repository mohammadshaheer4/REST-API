"""Serializers for the students app."""

from rest_framework import serializers

from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    """Serializer for the Student model."""

    class Meta:
        model = Student
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
