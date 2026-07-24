from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings

from app.models import Student, Course, Task, Event
from app.routes import students, courses, tasks, task_algorithms, events, event_algorithms


app = FastAPI(
    title=settings.APP_NAME,
    description="Student Academic Planner and Student Management System",
    version=settings.APP_VERSION
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    settings.FRONTEND_URL
],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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

app.include_router(
    task_algorithms.router
)

app.include_router(
    events.router
)

app.include_router(
    event_algorithms.router
)

@app.get(
    "/",
    tags=["System"]
)
def home():

    return {
        "message": "SAP-SMS Backend Running"
    }

