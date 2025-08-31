# Mandarin Learning API

## Overview

A FastAPI-based REST API for managing Mandarin Chinese learning content, including Hanzi characters, sentences, categories, and associated files. The application uses Tortoise ORM with SQLite for data persistence and follows a clean layered architecture pattern.

## Architecture

### Core Components

The application follows a 5-layer architecture pattern:

1. **Routes Layer** (`/app/routes/`) - FastAPI route handlers and API endpoints
2. **Manager Layer** (`/app/manager/`) - Business logic and orchestration
3. **Repository Layer** (`/app/repository/`) - Data access abstraction
4. **Schema Layer** (`/app/schema/`) - Pydantic models for request/response validation
5. **Config Layer** (`/app/config/`) - Application configuration and database setup

### Data Models

- **Hanzi**: Chinese characters with pinyin, meaning, HSK level, optional image and category
- **Sentence**: Chinese sentences with pinyin, meaning, category, and many-to-many relationship with Hanzis
- **Category**: Organizational units with HSK levels for grouping content
- **File**: File metadata with name and bucket information for image storage

### Key Features

- CRUD operations for all entities (Hanzi, Sentences, Categories, Files)
- HSK level-based filtering for structured learning progression
- Many-to-many relationships between sentences and Hanzi characters
- Image file association with Hanzi characters
- Pagination support for list endpoints

## Technology Stack

- **FastAPI** (0.104.1) - Modern, fast web framework for building APIs
- **Tortoise ORM** (0.20.0) - Async ORM inspired by Django ORM
- **Pydantic** (2.5.0) - Data validation and serialization
- **Pydantic Settings** (2.1.0) - Settings management with environment variables
- **Uvicorn** (0.24.0) - ASGI server for serving the application
- **SQLite** - Lightweight database with aiosqlite async driver
- **Docker** - Containerization with docker-compose for development
- **AWS S3** - Cloud storage for file management via boto3

## Project Structure

```
app/
├── config/           # Configuration and application setup
│   ├── app.py       # FastAPI app factory and router registration
│   ├── db.py        # Database connection and initialization
│   └── settings.py  # Environment-based configuration
├── integrations/    # External service integrations
│   └── s3.py        # AWS S3 service integration
├── manager/         # Business logic layer
│   ├── category_manager.py
│   ├── file_manager.py
│   ├── hanzi_manager.py
│   └── sentence_manager.py
├── repository/      # Data access layer
│   ├── models.py    # Tortoise ORM model definitions
│   ├── category_repository.py
│   ├── file_repository.py
│   ├── hanzi_repository.py
│   └── sentence_repository.py
├── routes/          # API route handlers
│   ├── category.py
│   ├── file.py
│   ├── hanzi.py
│   └── sentence.py
├── schema/          # Pydantic schemas for validation
│   ├── category_schema.py
│   ├── file_schema.py
│   ├── hanzi_schema.py
│   └── sentence_schema.py
└── main.py          # Application entry point
```

## API Endpoints

### Hanzi (Chinese Characters)
- `POST /api/hanzi/` - Create new Hanzi
- `GET /api/hanzi/{id}` - Get specific Hanzi by ID
- `GET /api/hanzi/` - List all Hanzis with pagination
- `GET /api/hanzi/hsk/{level}` - Get Hanzis by HSK level
- `GET /api/hanzi/category/{category_id}?hsk_level={level}` - Get Hanzis by category with optional HSK level filter
- `PUT /api/hanzi/{id}` - Update Hanzi
- `DELETE /api/hanzi/{id}` - Delete Hanzi

### Sentences
- `POST /api/sentences/` - Create new sentence
- `GET /api/sentences/{id}` - Get specific sentence by ID
- `GET /api/sentences/` - List all sentences with pagination
- `GET /api/sentences/category/{category_id}` - Get sentences by category
- `PUT /api/sentences/{id}` - Update sentence
- `DELETE /api/sentences/{id}` - Delete sentence

### Categories
- `POST /api/categories/` - Create new category
- `GET /api/categories/{id}` - Get specific category by ID
- `GET /api/categories/` - List all categories with pagination
- `GET /api/categories/hsk/{level}` - Get categories by HSK level
- `PUT /api/categories/{id}` - Update category
- `DELETE /api/categories/{id}` - Delete category

### Files
- `POST /api/files/` - Create new file record
- `GET /api/files/{id}` - Get specific file by ID
- `GET /api/files/{id}/content` - Get file content from S3 storage
- `DELETE /api/files/{id}` - Delete file record and S3 object

## Development

### Requirements

- Python 3.11+
- Dependencies listed in `requirements.txt`:
  - FastAPI 0.104.1
  - Uvicorn 0.24.0
  - Tortoise ORM 0.20.0
  - Pydantic 2.5.0
  - Pydantic Settings 2.1.0
  - python-dotenv 1.0.0
  - aiosqlite 0.19.0
  - boto3 1.34.0
  - black 23.12.1

### Running the Application

#### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# Or run directly with Python
python -m uvicorn app.main:app --reload
```

#### Docker Development
```bash
# Build and run with docker-compose
docker-compose up --build

# The API will be available at http://localhost:8000
```

### Configuration

The application uses environment-based configuration through Pydantic Settings:

- `DATABASE_URL` - Database connection string (default: `sqlite://./db.sqlite3`)
- `DEBUG` - Debug mode flag (default: `True`)
- `HOST` - Server host (default: `0.0.0.0`)
- `PORT` - Server port (default: `8000`)
- `AWS_ACCESS_KEY_ID` - AWS access key for S3 integration
- `AWS_SECRET_ACCESS_KEY` - AWS secret key for S3 integration
- `AWS_REGION` - AWS region for S3 bucket (default: `us-east-1`)
- `S3_BUCKET_NAME` - S3 bucket name for file storage

Configuration can be set via:
- Environment variables
- `.env` file (template available in `.env.example`)
- Direct modification of `app/config/settings.py`

### Database

- Uses SQLite as the default database
- Tortoise ORM handles schema generation automatically on startup
- Database file: `db.sqlite3` in the project root
- No migrations system is currently implemented

## Code Patterns and Conventions

### Architecture Patterns

1. **Repository Pattern**: Data access logic isolated in repository classes with static methods
2. **Manager Pattern**: Business logic encapsulated in manager classes that orchestrate repository calls
3. **Schema Separation**: Separate Pydantic schemas for create, update, and response operations
4. **Dependency Injection**: Managers instantiate their own repositories

### Naming Conventions

- **Files**: Snake_case (e.g., `hanzi_manager.py`)
- **Classes**: PascalCase (e.g., `HanziManager`)
- **Methods**: Snake_case (e.g., `create_hanzi`)
- **Variables**: Snake_case (e.g., `hanzi_data`)
- **API Endpoints**: Kebab-case with resource-based naming

### Code Patterns

- All repository methods are static and async
- Managers use dependency injection pattern for repositories
- Consistent error handling with HTTPException for 404 cases
- Pydantic models use `from_attributes = True` for ORM compatibility
- Foreign key relationships handled through optional IDs in schemas

### Data Access Patterns

- Eager loading with `prefetch_related` for related objects
- Pagination implemented with `skip` and `limit` parameters
- Soft relationship handling (optional foreign keys)
- Many-to-many relationships managed through Tortoise ORM's ManyToManyField

## API Documentation

The application includes built-in API documentation:
- **Swagger UI**: Available at `http://localhost:8000/docs`
- **ReDoc**: Available at `http://localhost:8000/redoc`
- **OpenAPI Schema**: Available at `http://localhost:8000/openapi.json`

## Domain Knowledge

This is a Mandarin Chinese learning application with the following educational concepts:

- **HSK Levels**: Hanyu Shuiping Kaoshi (Chinese Proficiency Test) levels 1-6
- **Hanzi**: Chinese characters with pronunciation (pinyin) and meaning
- **Sentences**: Example sentences containing Hanzi characters
- **Categories**: Thematic groupings aligned with HSK levels
- **Files**: Image resources associated with Hanzi for visual learning

The application supports structured learning progression through HSK levels and provides comprehensive CRUD operations for content management.