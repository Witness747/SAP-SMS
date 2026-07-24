from pydantic import BaseModel, ConfigDict


class StudentNested(BaseModel):

    student_id: int
    full_name: str
    email: str
    program: str | None = None

    model_config = ConfigDict(
        from_attributes=True
    )



class CourseCreate(BaseModel):

    student: StudentNested

    course_name: str

    course_code: str | None = None

    semester: int



class CourseResponse(CourseCreate):

    course_id: int

    student: StudentNested


    model_config = ConfigDict(
        from_attributes=True
    )