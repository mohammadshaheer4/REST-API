# Student API

A REST API for managing student records built with Django REST Framework.

## Features

- CRUD operations for students (Create, Read, Update, Delete)
- PostgreSQL database
- Health check endpoint

## Requirements

- Python 3.12+
- PostgreSQL
- [uv](https://github.com/astral-sh/uv) package manager

## Local Setup

1. **Clone the repository**

2. **Create environment file**

   Copy the example environment file and configure it:
   ```bash
   cp .env.example .env.local
   ```

   Update `.env.local` with your values:
   ```
   SECRET_KEY=<your-secret-key>
   DEBUG=True
   DATABASE_URL=postgres://<user>:<password>@localhost:5432/student_db
   ```

3. **Create the PostgreSQL database through PgAdmin**

4. **Install dependencies**
   ```bash
   make install
   ```

5. **Run migrations**
   ```bash
   make migrate
   ```

6. **Start the server**
   ```bash
   make run
   ```

   The API will be available at `http://localhost:8000`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/healthcheck/` | Health check |
| GET | `/api/students/` | List all students |
| POST | `/api/students/` | Create a student |
| GET | `/api/students/<id>/` | Get a student |
| PUT | `/api/students/<id>/` | Update a student |
| DELETE | `/api/students/<id>/` | Delete a student |

## Student Schema

| Field | Type | Description |
|-------|------|-------------|
| id | integer | Auto-generated ID |
| first_name | string | First name (max 100 chars) |
| last_name | string | Last name (max 100 chars) |
| email | string | Email address (unique) |
| date_of_birth | date | Date of birth (YYYY-MM-DD) |
| created_at | datetime | Record creation timestamp |
| updated_at | datetime | Last update timestamp |

## Make Commands

- `make install` - Install dependencies
- `make migrate` - Run database migrations
- `make run` - Start the development server
- `make test` - Run tests
- `make lint` - Check for syntax errors