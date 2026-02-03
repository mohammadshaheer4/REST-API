"""Tests for the students app."""

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .models import Student


class HealthCheckTest(TestCase):
    """Tests for the health check endpoint."""

    def test_healthcheck(self):
        """Test that health check returns OK status."""
        client = APIClient()
        response = client.get("/healthcheck")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "ok")


class StudentAPITest(TestCase):
    """Tests for the Student API endpoints."""

    def setUp(self):
        """Set up test data."""
        self.client = APIClient()
        self.student_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "date_of_birth": "2000-01-15",
        }
        self.student = Student.objects.create(
            first_name="Jane",
            last_name="Smith",
            email="jane.smith@example.com",
            date_of_birth="1999-05-20",
        )

    def test_create_student(self):
        """Test creating a student with valid data."""
        response = self.client.post(
            "/api/v1/students/", self.student_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["first_name"], "John")
        self.assertEqual(response.data["email"], "john.doe@example.com")

    def test_create_student_invalid(self):
        """Test creating a student with missing required fields."""
        response = self.client.post(
            "/api/v1/students/", {"first_name": "No"}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_student_duplicate_email(self):
        """Test creating a student with a duplicate email address."""
        data = self.student_data.copy()
        data["email"] = "jane.smith@example.com"
        response = self.client.post(
            "/api/v1/students/", data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_students(self):
        """Test listing all students."""
        response = self.client.get("/api/v1/students/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_student(self):
        """Test retrieving a single student by ID."""
        response = self.client.get(f"/api/v1/students/{self.student.pk}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["first_name"], "Jane")

    def test_get_student_not_found(self):
        """Test retrieving a non-existent student returns 404."""
        response = self.client.get("/api/v1/students/9999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_student(self):
        """Test updating a student with valid data."""
        updated = {
            "first_name": "Janet",
            "last_name": "Smith",
            "email": "janet.smith@example.com",
            "date_of_birth": "1999-05-20",
        }
        response = self.client.put(
            f"/api/v1/students/{self.student.pk}/", updated, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["first_name"], "Janet")

    def test_update_student_invalid(self):
        """Test updating a student with missing required fields."""
        response = self.client.put(
            f"/api/v1/students/{self.student.pk}/",
            {"first_name": "Janet"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_student(self):
        """Test deleting a student."""
        response = self.client.delete(f"/api/v1/students/{self.student.pk}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Student.objects.count(), 0)

    def test_delete_student_not_found(self):
        """Test deleting a non-existent student returns 404."""
        response = self.client.delete("/api/v1/students/9999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
