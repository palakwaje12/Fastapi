# FastAPI – Student Data API

A beginner-friendly backend development project built using **Python, FastAPI, and JSON**. This project focuses on understanding REST API fundamentals, HTTP methods, endpoints, path parameters, query parameters, sorting, input validation, and pagination.

This repository documents my journey of learning FastAPI and backend development through hands-on practice.

## 🚀 Technologies Used

- **Python** – Backend programming
- **FastAPI** – Building REST APIs
- **JSON** – Storing and retrieving student data
- **Uvicorn** – Running the FastAPI application
- **VS Code** – Development environment

## 📂 Project Structure

```text
FastAPI/
│
├── main.py
├── student-data.json
└── README.md
```

## 📌 Concepts Implemented

### 1. Creating a FastAPI Application
- Importing FastAPI.
- Creating a FastAPI application instance.
- Understanding how backend applications work.

### 2. HTTP Methods

Understanding the basic HTTP methods used in API development:

| Method | Purpose |
|---|---|
| GET | Retrieve data |
| POST | Create new data |
| PUT | Update existing data |
| DELETE | Delete data |

*Currently, the project focuses on GET requests.*

### 3. Creating API Endpoints

Implemented different GET endpoints:

| Endpoint | Description |
|---|---|
| `/` | Root endpoint |
| `/hello` | Returns a welcome message |
| `/student` | Fetches all student records |
| `/student/{students_id}` | Fetches a particular student using their ID |

### 4. Working with JSON Data

- Loading student records from a JSON file.
- Using Python's built-in `json` module.
- Creating a helper function `load_data()` to read JSON data.
- Understanding how Python interacts with JSON files.

### 5. Path Parameters

Implemented dynamic student ID retrieval.

Example:

```http
GET /student/001
```

This endpoint retrieves the student record corresponding to ID `001`.

### 6. Query Parameters

Understanding how query parameters are passed through URLs to customize API responses.

Example:

```http
GET /sort?sort_by=age&order=asc
```

### 7. Sorting Student Records

Implemented sorting functionality using Python's `sorted()` function and lambda expressions.

Supported sorting fields:
- Age
- Grades

Supported sorting orders:
- Ascending (`asc`)
- Descending (`desc`)

Invalid sorting fields and sorting orders are handled using FastAPI's `HTTPException`.

### 8. Input Validation and Exception Handling

Used `HTTPException` to handle invalid inputs and return meaningful error messages with appropriate HTTP status codes.

### 9. Pagination

Implemented pagination to retrieve student records in smaller portions instead of returning the entire dataset.

Example:

```http
GET /paginate?page=1&limit=2
```

Where:
- `page` represents the page number.
- `limit` represents the number of records per page.

Pagination logic:

```python
start = (page - 1) * limit
end = start + limit
```

## ▶️ How to Run the Project

### Step 1: Clone the Repository

```bash
git clone <your-repository-link>
```

### Step 2: Navigate to the Project Folder

```bash
cd FastAPI
```

### Step 3: Install Dependencies

```bash
pip install fastapi uvicorn
```

### Step 4: Start the Server

```bash
uvicorn main:app --reload
```

### Step 5: Explore the API

Open the following URLs in your browser:

- Application: http://127.0.0.1:8000
- Interactive Swagger Documentation: http://127.0.0.1:8000/docs
- ReDoc Documentation: http://127.0.0.1:8000/redoc

## 🎯 Learning Objectives

Through this project, I am developing an understanding of:

- Backend development using Python.
- REST API fundamentals.
- HTTP request methods and API endpoints.
- Working with path and query parameters.
- Reading and processing JSON data.
- Sorting and pagination.
- Input validation and exception handling.
- Testing APIs using Swagger UI.

## 📈 Future Learning Goals

As I continue learning FastAPI, I plan to explore:

- POST, PUT, and DELETE operations.
- Pydantic models and request body validation.
- CRUD operations.
- MySQL database integration.
- Authentication and authorization.
- Building more complex REST APIs.
- Deploying backend applications.

## 👩‍💻 Learning Journey

This repository is part of my journey into Python backend development. I am learning FastAPI step by step by implementing concepts and practising them through small projects.

**More concepts and implementations will be added as I progress!**
