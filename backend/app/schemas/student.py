from pydantic import BaseModel


class StudentBase(BaseModel):

    full_name: str
    email: str
    program: str


class StudentCreate(StudentBase):
    pass


class StudentResponse(StudentBase):

    student_id: int

    class Config:
        from_attributes = True