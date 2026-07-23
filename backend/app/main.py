from fastapi import FastAPI

from app.models import Student, Course, Task, Event
from app.routes import students
from app.routes import students, courses

app = FastAPI(
    title="SAP-SMS API",
    description="Student Academic Planner and Student Management System",
    version="1.0.0"
)

app.include_router(
    students.router
)

app.include_router(
    courses.router
)

@app.get("/")
def home():
    return {
        "message": "SAP-SMS Backend Running"
    }