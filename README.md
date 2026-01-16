# Adaptive MCQ Testing System - Django Backend

An intelligent adaptive multiple-choice question (MCQ) testing system built with Django and Django REST Framework. This backend uses machine learning algorithms (Item Response Theory) to dynamically adapt questions based on student performance and proficiency levels.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Database Schema](#database-schema)
- [Machine Learning Models](#machine-learning-models)
- [Docker Setup](#docker-setup)
- [Contributing](#contributing)
- [License](#license)

## Features

✨ **Adaptive Learning**
- Personalized MCQ selection based on student proficiency levels
- Intelligent difficulty adjustment using Item Response Theory (IRT) algorithm
- Real-time difficulty calculation for questions

🧠 **Student Analytics**
- Comprehensive user performance tracking
- User proficiency scoring and analysis
- Question-level analytics and success rates
- Student progress monitoring

📊 **Data Management**
- Multi-specialization support (e.g., different subjects/courses)
- Course and level of education management
- Flexible question categorization with attachments

🏗️ **Clean Architecture**
- RESTful API design using Django REST Framework
- Modular app-based structure
- CORS support for frontend integration
- PostgreSQL database with Docker support

## Project Structure

```
SIH_adaptive_learning/
├── courses/                    # Course management app
│   ├── models.py              # Course data models
│   ├── views.py               # Course API endpoints
│   ├── serializers.py         # DRF serializers
│   └── urls.py                # URL routing
├── questions/                 # Question management app
│   ├── models.py              # Question and Options models
│   ├── views.py               # Question API endpoints
│   ├── controller.py          # Question selection logic
│   └── migrations/
├── student/                   # Student management app
│   ├── models.py              # Student data model
│   ├── views.py               # Student API endpoints
│   └── serializers.py
├── user_analytics/            # User performance tracking
│   ├── models.py              # Analytics data models
│   ├── views.py               # Analytics endpoints
│   └── serializers.py
├── question_analytics/        # Question-level analytics
│   ├── models.py              # Question performance data
│   └── views.py
├── specializations/           # Subject/Specialization management
│   ├── models.py
│   └── views.py
├── level_of_education/        # Education level (Grade/Semester)
│   ├── models.py
│   └── views.py
├── parakh_test/              # Test management module
├── test_question/            # Test question linking
├── ml_models/                # Machine learning module
│   ├── algorithms/           # Algorithm implementations
│   │   ├── IRT.py           # Item Response Theory algorithm
│   │   └── Pre-Assessment_Dataset/
│   ├── controller.py
│   └── views.py
└── SIH_adaptive_learning/    # Django project settings
    ├── settings.py           # Django configuration
    ├── urls.py               # URL routing
    ├── asgi.py               # ASGI config
    └── wsgi.py               # WSGI config
```

## Prerequisites

- **Python**: 3.9 or higher
- **Django**: 4.2.5
- **PostgreSQL**: 12 or higher (optional, SQLite for development)
- **Docker & Docker Compose**: For containerized development (optional)
- **pip**: Python package manager

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Django-Backend
```

### 2. Create a Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Navigate to Project Directory

```bash
cd SIH_adaptive_learning
```

## Configuration

### Environment Setup

The project uses Django's settings module. Key configurations are in `SIH_adaptive_learning/settings.py`:

**Default Configuration:**
- **DEBUG**: True (for development)
- **ALLOWED_HOSTS**: "*" (configure for production)
- **Database**: SQLite by default (can be switched to PostgreSQL)
- **CORS Origins**: `http://localhost:*` and `https://localhost:*`

### Database Configuration

**For PostgreSQL** (uncomment in `settings.py`):

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sih1',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': '127.0.0.1',
        'PORT': '5450',
    }
}
```

**For SQLite** (default):

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

## Running the Application

### 1. Apply Migrations

```bash
python manage.py migrate
```

### 2. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 3. Load Sample Data (If Available)

```bash
# For PostgreSQL, use the SQL dump
psql -U postgres -d sih1 -f SIH_dump.sql
```

### 4. Run Development Server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

### 5. Access Admin Panel

```
http://127.0.0.1:8000/admin/
```

## API Documentation

### Base URL

```
http://localhost:8000/api/
```

### Key Endpoints

#### Questions API
- `GET /questions/get/` - Get adaptive MCQ based on student proficiency
- `POST /questions/create/` - Create new question
- `GET /questions/list/` - List all questions

**Parameters:**
```json
{
  "student_id": 1,
  "specialization_id": "subject_1"
}
```

#### Student API
- `GET /student/` - List all students
- `POST /student/` - Create new student
- `GET /student/{id}/` - Get student details

#### User Analytics API
- `GET /user_analytics/` - Get user performance metrics
- `POST /user_analytics/` - Create user analysis record

#### Courses API
- `GET /courses/` - List all courses
- `POST /courses/` - Create new course

#### Specializations API
- `GET /specializations/` - List all specializations
- `POST /specializations/` - Create new specialization

### Response Format

**Success Response:**
```json
{
  "success": true,
  "data": {
    "question_id": "q1",
    "title": "Question text",
    "options": [
      {
        "option_id": "opt1",
        "option_title": "Option 1"
      }
    ],
    "difficulty": 0.65
  }
}
```

**Error Response:**
```json
{
  "success": false,
  "error": "Error message"
}
```

## Database Schema

### Core Models

**Student**
- `student_id` (Primary Key)
- `student_name`

**Questions**
- `id` (Primary Key, TextField)
- `title` (TextField)
- `attachment` (TextField for media/images)
- `options` (Many-to-Many with Options)
- `answer_id` (Foreign Key to Options)
- `specialization` (Foreign Key to Specialization)
- `difficulty` (Float, default 0.5)

**Options**
- `option_id` (Primary Key)
- `option_title`
- `option_attachment`

**User_analysis**
- `student_id` (Foreign Key)
- `specialization` (Foreign Key)
- `user_proficiency` (Proficiency score)

**Specialization**
- `specialization_id` (Primary Key)
- `specialization_name`

## Machine Learning Models

### Item Response Theory (IRT)

The system implements the IRT algorithm for intelligent question selection and difficulty assessment.

**Location:** `ml_models/algorithms/IRT.py`

**Features:**
- Calculates student ability parameter (θ)
- Estimates question difficulty and discrimination
- Predicts probability of correct response
- Adapts question difficulty based on performance

**Usage:**
```python
from ml_models.algorithms.IRT import calculate_proficiency
proficiency = calculate_proficiency(user_analysis)
```

**Pre-Assessment Dataset:**
- Located in `ml_models/algorithms/Pre-Assessment_Dataset/`
- Contains categorized questions for baseline assessment
- Supports CSV format data import

## Docker Setup

### Using Docker Compose

**1. Build and Run Containers:**

```bash
docker-compose up -d
```

This will:
- Start PostgreSQL database on port 5450
- Initialize database with `SIH_dump.sql`

**2. Run Django Migrations (First time only):**

```bash
docker exec <container_name> python manage.py migrate
```

**3. Access the Application:**

```
Backend API: http://localhost:8000/
Database: localhost:5450
```

**4. Stop Containers:**

```bash
docker-compose down
```

### Dockerfile Configuration

The PostgreSQL container is configured in `docker-compose.yaml`:
- **Database**: sih1
- **User**: postgres
- **Port**: 5450
- **Password**: configured in docker-compose.yaml

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| Django | 4.2.5 | Web framework |
| djangorestframework | 3.14.0 | REST API framework |
| psycopg2 | 2.9.7 | PostgreSQL adapter |
| django-cors-headers | - | CORS support |
| django-filter | 23.3 | Query filtering |
| PyJWT | 2.8.0 | JWT authentication |
| django-environ | 0.11.2 | Environment variable management |

See `requirements.txt` for complete dependency list.

## Development Workflow

### Adding New Features

1. Create a new app:
   ```bash
   python manage.py startapp app_name
   ```

2. Define models in `models.py`

3. Create serializers in `serializers.py`

4. Implement views in `views.py`

5. Add URL routing in `urls.py`

6. Create migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

### Running Tests

```bash
python manage.py test
```

### Linting and Code Quality

```bash
python manage.py check
```

## Deployment Considerations

**For Production:**
- Set `DEBUG = False` in settings.py
- Update `ALLOWED_HOSTS` with your domain
- Use environment variables for sensitive data
- Configure proper CORS origins
- Use production-grade database (PostgreSQL recommended)
- Set up HTTPS/SSL
- Use Gunicorn or uWSGI for application server
- Configure static file serving (Whitenoise or CloudFront)

**Example Production Configuration:**

```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

## Troubleshooting

### Common Issues

**Issue: "No module named 'django'"**
- Solution: Ensure virtual environment is activated and requirements are installed

**Issue: "PostgreSQL connection refused"**
- Solution: Verify PostgreSQL is running and connection credentials are correct

**Issue: "ModuleNotFoundError in migrations"**
- Solution: Run `python manage.py makemigrations` followed by `python manage.py migrate`

**Issue: CORS errors**
- Solution: Check `CORS_ALLOWED_ORIGINS` in settings.py

## Project Information

- **Project Name**: Adaptive MCQ Testing System
- **Backend Framework**: Django 4.2.5
- **API**: Django REST Framework
- **Database**: PostgreSQL (default) / SQLite (development)
- **Python Version**: 3.9+
- **Machine Learning**: Item Response Theory (IRT)

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact & Support

For issues, questions, or suggestions, please:
- Open an issue in the GitHub repository
- Contact the development team

---
