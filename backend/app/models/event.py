from sqlalchemy import Column, Integer, String, Date, Time, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
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
        String(255),
        nullable=False
    )


    event_type = Column(
        String(100),
        nullable=True
    )


    event_date = Column(
        Date,
        nullable=False
    )


    start_time = Column(
        Time,
        nullable=False
    )


    end_time = Column(
        Time,
        nullable=False
    )


    location = Column(
        String(255),
        nullable=True
    )


    created_at = Column(
        DateTime,
        server_default=func.now()
    )

    # Relationships
    student = relationship(
        "Student",
        back_populates="events"
    )