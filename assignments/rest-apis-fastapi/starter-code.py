from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# TODO: Define the Student model with id, name, and grade fields
class Student(BaseModel):
    pass


# In-memory store
students = []


# TODO: Implement GET / - return a welcome message
@app.get("/")
def root():
    pass


# TODO: Implement GET /students - return all students
# Bonus: accept an optional `grade` query parameter to filter results
@app.get("/students")
def get_students():
    pass


# TODO: Implement POST /students - add a new student
@app.post("/students")
def create_student(student: Student):
    pass


# TODO: Implement GET /students/{id} - return a student by ID, or 404 if not found
@app.get("/students/{student_id}")
def get_student(student_id: int):
    pass


# TODO: Implement DELETE /students/{id} - remove a student by ID, or 404 if not found
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    pass
