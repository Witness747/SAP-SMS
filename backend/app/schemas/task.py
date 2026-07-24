from datetime import date, datetime

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator
)


class StudentNested(BaseModel):

    student_id: int
    full_name: str
    email: str
    program: str | None = None


    model_config = ConfigDict(
        from_attributes=True
    )



class TaskBase(BaseModel):

    title: str = Field(
        ...,
        min_length=3,
        max_length=255
    )

    priority: str

    status: str

    due_date: date



class TaskCreate(TaskBase):
    pass



class TaskResponse(TaskBase):

    task_id: int

    student: StudentNested

    created_at: datetime


    model_config = ConfigDict(
        from_attributes=True
    )