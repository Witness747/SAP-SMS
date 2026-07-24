from datetime import datetime

from pydantic import BaseModel, ConfigDict


class StudentBase(BaseModel):

    full_name: str
    email: str
    program: str | None = None



class StudentCreate(StudentBase):
    pass



class StudentResponse(StudentBase):

    student_id: int
    created_at: datetime


    model_config = ConfigDict(
        from_attributes=True
    )