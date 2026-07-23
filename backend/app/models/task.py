from sqlalchemy import Column, Integer, String, Date, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func

from app.database.database import Base


class Task(Base):

    __tablename__ = "tasks"

    task_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    student_id = Column(
        Integer,
        ForeignKey("students.student_id"),
        nullable=False
    )

    title = Column(
        String(150),
        nullable=False
    )

    priority = Column(
        String(20),
        nullable=False
    )

    status = Column(
        String(20),
        default="Pending"
    )

    due_date = Column(
        Date
    )

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )