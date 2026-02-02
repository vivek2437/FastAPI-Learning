# FastAPI CRUD Application

A FastAPI project demonstrating CRUD (Create, Read, Update, Delete) operations with a book management system.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Sample Data](#sample-data)
- [Technologies](#technologies)
- [How to Use](#how-to-use)

## Features

- **Create** - Add new books to the collection
- **Read** - Retrieve all books or a specific book by ID
- **Update** - Modify existing book information
- **Delete** - Remove books from the collection
- **Error Handling** - HTTP exceptions for invalid requests
- **Data Validation** - Pydantic models for request/response validation
- **Interactive API Docs** - Auto-generated Swagger UI and ReDoc

## Project Structure

```
d:\New folder\
├── crud.py          # Main CRUD application with FastAPI
├── README.md        # Project documentation
└── requirements.txt # Project dependencies
```

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup Steps

1. Navigate to the project directory:
   ```bash
   cd d:\New folder
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install required dependencies:
   ```bash
   pip install fastapi uvicorn
   ```

   Or install from requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Start the FastAPI development server:

```bash
uvicorn crud:app --reload
```

The server will start at `http://127.0.0.1:8000`

The `--reload` flag enables auto-restart when code changes are detected.

## API Endpoints

### Get All Books

**Request:**
```
GET /book
```

**Response:**
```json
[
  {
    "id": 1,
    "title": "1984",
    "author": "George Orwell",
    "year_published": 1949
  },
  ...
]
```

### Get Book by ID

**Request:**
```
GET /book/{book_id}
```

**Example:**
```
GET /book/1
```

**Response (Success):**
```json
{
  "id": 1,
  "title": "1984",
  "author": "George Orwell",
  "year_published": 1949
}
```

**Response (Not Found):**
```json
{
  "detail": "Book with the id 999 not found"
}
```

### Create a New Book

**Request:**
```
POST /book
Content-Type: application/json

{
  "id": 5,
  "title": "Brave New World",
  "author": "Aldous Huxley",
  "year_published": 1932
}
```

**Response:**
```json
{
  "id": 5,
  "title": "Brave New World",
  "author": "Aldous Huxley",
  "year_published": 1932
}
```

### Update a Book

**Request:**
```
PUT /book/{book_id}
Content-Type: application/json

{
  "id": 1,
  "title": "1984 (Revised)",
  "author": "George Orwell",
  "year_published": 1949
}
```

**Example:**
```
PUT /book/1
```

**Response (Success):**
```json
{
  "id": 1,
  "title": "1984 (Revised)",
  "author": "George Orwell",
  "year_published": 1949
}
```

**Response (Not Found):**
```json
{
  "detail": "Book with the id 999 not found"
}
```

### Delete a Book

**Request:**
```
DELETE /book/{book_id}
```

**Example:**
```
DELETE /book/1
```

**Response (Success):**
```json
{
  "detail": "Book with id 1 deleted",
  "book": {
    "id": 1,
    "title": "1984",
    "author": "George Orwell",
    "year_published": 1949
  }
}
```

**Response (Not Found):**
```json
{
  "detail": "Book with the id 999 not found"
}
```

## Sample Data

The API comes pre-loaded with 4 classic books:

| ID | Title | Author | Year |
|----|-------|--------|------|
| 1 | 1984 | George Orwell | 1949 |
| 2 | To Kill a Mockingbird | Harper Lee | 1960 |
| 3 | The Great Gatsby | F. Scott Fitzgerald | 1925 |
| 4 | Pride and Prejudice | Jane Austen | 1813 |

## Technologies

- **FastAPI** - Modern web framework for building APIs with Python
- **Uvicorn** - ASGI server implementation
- **Pydantic** - Data validation using Python type annotations
- **Starlette** - The underlying framework for FastAPI

## How to Use

### Using the Interactive API Documentation

1. Start the server with `uvicorn crud:app --reload`
2. Open your browser and navigate to:
   - **Swagger UI:** `http://127.0.0.1:8000/docs`
   - **ReDoc:** `http://127.0.0.1:8000/redoc`

3. Test the endpoints directly from the documentation interface

### Using cURL

```bash
# Get all books
curl -X GET "http://127.0.0.1:8000/book"

# Get a specific book
curl -X GET "http://127.0.0.1:8000/book/1"

# Create a new book
curl -X POST "http://127.0.0.1:8000/book" \
  -H "Content-Type: application/json" \
  -d '{"id":5,"title":"Brave New World","author":"Aldous Huxley","year_published":1932}'

# Update a book
curl -X PUT "http://127.0.0.1:8000/book/1" \
  -H "Content-Type: application/json" \
  -d '{"id":1,"title":"1984 Updated","author":"George Orwell","year_published":1949}'

# Delete a book
curl -X DELETE "http://127.0.0.1:8000/book/1"
```

### Using Python Requests

```python
import requests

BASE_URL = "http://127.0.0.1:8000"

# Get all books
response = requests.get(f"{BASE_URL}/book")
print(response.json())

# Create a new book
new_book = {
    "id": 5,
    "title": "Brave New World",
    "author": "Aldous Huxley",
    "year_published": 1932
}
response = requests.post(f"{BASE_URL}/book", json=new_book)
print(response.json())

# Update a book
updated_book = {
    "id": 1,
    "title": "1984 Updated",
    "author": "George Orwell",
    "year_published": 1949
}
response = requests.put(f"{BASE_URL}/book/1", json=updated_book)
print(response.json())

# Delete a book
response = requests.delete(f"{BASE_URL}/book/1")
print(response.json())
```

## Error Handling

The API returns appropriate HTTP status codes:

- **200 OK** - Successful GET, PUT requests
- **201 Created** - Successful POST request
- **404 Not Found** - Book with specified ID doesn't exist
- **422 Unprocessable Entity** - Invalid request data

## Future Improvements

- Add database persistence (SQLAlchemy with SQLite/PostgreSQL)
- Implement authentication and authorization
- Add pagination for large datasets
- Add filtering and sorting capabilities
- Write unit tests
- Add logging functionality

## Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [HTTP Status Codes](https://httpwg.org/specs/rfc7231.html#status.codes)
- [REST API Best Practices](https://restfulapi.net/)

## License

This project is open source and available for educational purposes.

---

**Created:** February 2, 2026