from fastapi import FastAPI

from app.models import Student, Course, Task, Event
from app.routes import students

app = FastAPI(
    title="SAP-SMS API",
    description="Student Academic Planner and Student Management System",
    version="1.0.0"
)

app.include_router(
    students.router
)


@app.get("/")
def home():
    return {
        "message": "SAP-SMS Backend Running"
    }