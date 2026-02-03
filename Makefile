.PHONY: install migrate run test lint

install:
	uv sync

migrate:
	uv run python manage.py makemigrations
	uv run python manage.py migrate

run:
	uv run python manage.py runserver 0.0.0.0:8000

test:
	uv run python manage.py test students

lint:
	uv run python -m py_compile manage.py
	uv run python -m py_compile student_api/settings.py
	uv run python -m py_compile students/models.py
	uv run python -m py_compile students/views.py
	uv run python -m py_compile students/serializers.py
	uv run python -m py_compile students/tests.py
