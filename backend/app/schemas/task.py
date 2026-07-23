from pydantic import BaseModel
from datetime import date, datetime


class TaskBase(BaseModel):

    title: str
    priority: str
    status: str
    due_date: date


class TaskCreate(TaskBase):
    pass


class TaskResponse(TaskBase):

    task_id: int
    student_id: int
    created_at: datetime

    class Config:
        from_attributes = True