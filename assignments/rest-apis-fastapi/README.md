# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a REST API using the FastAPI framework by creating endpoints that handle HTTP requests, return JSON responses, and validate data using Python type hints.

## 📝 Tasks

### 🛠️ Set Up a FastAPI App and Create Your First Endpoint

#### Description
Install FastAPI and create a basic application with a root endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Import and initialize a `FastAPI` app instance
- Define a `GET /` endpoint that returns a JSON response with a welcome message
- Run the app using `uvicorn` and confirm it responds in the browser or via `curl`


### 🛠️ Build a Students CRUD API

#### Description
Extend the app with endpoints to create, read, update, and delete student records stored in an in-memory list or dictionary.

#### Requirements
Completed program should:

- Define a `Student` model using `pydantic.BaseModel` with fields: `id`, `name`, and `grade`
- Implement `GET /students` to return all students
- Implement `POST /students` to add a new student
- Implement `GET /students/{id}` to retrieve a student by ID
- Implement `DELETE /students/{id}` to remove a student by ID
- Return appropriate HTTP status codes (e.g., `404` when a student is not found)


### 🛠️ Add Query Parameters and Filtering

#### Description
Add the ability to filter students by grade using a query parameter on the list endpoint.

#### Requirements
Completed program should:

- Accept an optional `grade` query parameter on `GET /students`
- Return only students matching the given grade when the parameter is provided
- Return all students when no filter is specified

Example:
```
GET /students?grade=A  →  returns only students with grade "A"
GET /students          →  returns all students
```
