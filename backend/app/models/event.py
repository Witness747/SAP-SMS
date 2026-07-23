from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func

from app.database.database import Base


class Event(Base):

    __tablename__ = "events"

    event_id = Column(
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

    event_type = Column(
        String(50)
    )

    start_time = Column(
        TIMESTAMP,
        nullable=False
    )

    end_time = Column(
        TIMESTAMP,
        nullable=False
    )

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )