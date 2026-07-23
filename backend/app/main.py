from fastapi import FastAPI

from app.models import Student, Course, Task, Event
from app.routes import students, courses,tasks 


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

app.include_router(
    tasks.router
)

@app.get(
    "/",
    tags=["System"]
)
def home():

    return {
        "message": "SAP-SMS Backend Running"
    }

