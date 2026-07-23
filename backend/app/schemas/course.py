from pydantic import BaseModel


class CourseBase(BaseModel):

    course_name: str
    course_code: str
    semester: int


class CourseCreate(CourseBase):
    pass


class CourseResponse(CourseBase):

    course_id: int
    student_id: int

    class Config:
        from_attributes = True

        