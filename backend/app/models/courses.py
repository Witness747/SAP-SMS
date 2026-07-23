from sqlalchemy import Column, Integer, String, ForeignKey

from app.database.database import Base


class Course(Base):

    __tablename__ = "courses"

    course_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    student_id = Column(
        Integer,
        ForeignKey("students.student_id"),
        nullable=False
    )

    course_name = Column(
        String(100),
        nullable=False
    )

    course_code = Column(
        String(20)
    )

    semester = Column(
        Integer
    )