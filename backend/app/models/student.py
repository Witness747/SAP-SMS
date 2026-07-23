from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func

from app.database.database import Base


class Student(Base):

    __tablename__ = "students"

    student_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    full_name = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(100),
        unique=True,
        nullable=False
    )

    program = Column(
        String(100)
    )

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )