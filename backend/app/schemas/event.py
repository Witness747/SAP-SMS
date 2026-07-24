from datetime import date, time, datetime

from pydantic import BaseModel, ConfigDict


# Schema used when creating a new event
class EventCreate(BaseModel):

    student_id: int

    title: str

    event_type: str | None = None

    event_date: date

    start_time: time

    end_time: time

    location: str | None = None



# Schema used when returning event data
class EventResponse(BaseModel):

    event_id: int

    student_id: int

    title: str

    event_type: str | None = None

    event_date: date

    start_time: time

    end_time: time

    location: str | None = None

    created_at: datetime


    model_config = ConfigDict(
        from_attributes=True
    )