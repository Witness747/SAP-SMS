from pydantic import BaseModel
from datetime import date

class EventConflictResponse(BaseModel):

    event_1: str

    event_2: str

    date: date

    message: str