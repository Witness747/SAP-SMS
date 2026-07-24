from datetime import date
from pydantic import BaseModel, ConfigDict


class TaskAlgorithmResponse(BaseModel):

    title: str
    due_date: date

    model_config = ConfigDict(
        from_attributes=True
    )

class TaskSearchResponse(BaseModel):

    title: str

    model_config = ConfigDict(
        from_attributes=True
    )

class TaskPriorityResponse(BaseModel):

    title: str
    priority: str

    model_config = ConfigDict(
        from_attributes=True
    )