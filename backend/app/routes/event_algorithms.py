from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependency import get_db
from app.models import Event

from app.schemas.event_algorithm import (
    EventConflictResponse
)

from app.services.event_algorithms import (
    detect_event_conflicts
)


router = APIRouter(

    prefix="/event-algorithms",

    tags=["Event Algorithms"]

)


@router.get(

    "/conflicts",

    response_model=list[
        EventConflictResponse
    ]

)
def get_event_conflicts(

    db: Session = Depends(get_db)

):

    events = db.query(Event).all()

    conflicts = detect_event_conflicts(
        events
    )

    return conflicts

