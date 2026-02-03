# Student API

A REST API for managing student records built with Django REST Framework.

## Features

- CRUD operations for students (Create, Read, Update, Delete)
- PostgreSQL database
- Health check endpoint

## Docker Setup

1. **Create environment file**
   ```bash
   cp .env.example .env.local
   ```
   Update `SECRET_KEY` and `DEBUG` in `.env.local`. The `DATABASE_URL` is configured by Docker Compose.

2. **Build and start containers**
   ```bash
   make docker-build
   ```

3. **Run migrations**
   ```bash
   make docker-migrate
   ```

4. **View logs**
   ```bash
   make docker-logs
   ```

5. **Stop containers**
   ```bash
   make docker-down
   ```

## Local setup (wihtout docker)

1. **Create environment file**
   ```bash
   cp .env.example .env.local
   ```
   Update `SECRET_KEY`, `DEBUG`, and `DATABASE_URL` in `.env.local`.

2. **Install dependencies**
   ```bash
   make install
   ```

3. **Run migrations**
   ```bash
   make migrate
   ```

4. **Run server**
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

### Docker
- `make docker-build` - Build and start containers
- `make docker-migrate` - Run database migrations
- `make docker-logs` - View container logs
- `make docker-down` - Stop containers

### Local Development
- `make install` - Install dependencies
- `make migrate` - Run database migrations
- `make run` - Start the development server
- `make test` - Run tests
- `make lint` - Check for syntax errors