from datetime import date, time, datetime

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
    model_validator
)

class StudentNested(BaseModel):

    student_id: int
    full_name: str
    email: str


    model_config = ConfigDict(
        from_attributes=True
    )



class EventCreate(BaseModel):

    student: StudentNested

    title: str = Field(
        ...,
        min_length=3,
        max_length=255
    )

    event_type: str | None = Field(
        default=None,
        max_length=100
    )

    event_date: date

    start_time: time

    end_time: time

    location: str | None = Field(
        default=None,
        max_length=255
    )


    @field_validator("title")
    @classmethod
    def validate_title(cls, value):

        if not value.strip():
            raise ValueError(
                "Title cannot be empty"
            )

        return value



    @model_validator(mode="after")
    def validate_event_time(self):

        if self.end_time <= self.start_time:

            raise ValueError(
                "End time must be after start time"
            )

        return self



class EventResponse(BaseModel):

    event_id: int

    title: str

    event_type: str | None = None

    event_date: date

    start_time: time

    end_time: time

    location: str | None = None

    student: StudentNested

    created_at: datetime


    model_config = ConfigDict(
        from_attributes=True
    )


