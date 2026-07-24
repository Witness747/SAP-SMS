from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi import Query
from app.schemas.pagination import PaginationResponse
from app.database.dependency import get_db
from app.models import Event
from app.schemas.event import EventCreate, EventResponse
from app.core.exceptions import not_found_error

router = APIRouter(
    prefix="/events",
    tags=["Events"]
)


# CREATE EVENT
@router.post(
    "/",
    response_model=EventResponse
)
def create_event(
    event: EventCreate,
    db: Session = Depends(get_db)
):

    new_event = Event(
        student_id=event.student_id,
        title=event.title,
        event_type=event.event_type,
        event_date=event.event_date,
        start_time=event.start_time,
        end_time=event.end_time,
        location=event.location
    )


    db.add(new_event)

    db.commit()

    db.refresh(new_event)


    return new_event



# READ ALL EVENTS
@router.get(
    "/",
    response_model=PaginationResponse[EventResponse]
)
def get_events(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):

    skip = (page - 1) * limit

    total = db.query(Event).count()

    events = (
        db.query(Event)
        .offset(skip)
        .limit(limit)
        .all()
    )

    return PaginationResponse(
        total=total,
        page=page,
        limit=limit,
        data=events
    )



# READ SINGLE EVENT
@router.get(
    "/{event_id}",
    response_model=EventResponse
)
def get_event(
    event_id: int,
    db: Session = Depends(get_db)
):

    event = (
        db.query(Event)
        .filter(Event.event_id == event_id)
        .first()
    )


    if not event:
        not_found_error("Event", event_id)


    return event



# UPDATE EVENT
@router.put(
    "/{event_id}",
    response_model=EventResponse
)
def update_event(
    event_id: int,
    event_data: EventCreate,
    db: Session = Depends(get_db)
):

    event = (
        db.query(Event)
        .filter(Event.event_id == event_id)
        .first()
    )


    if not event:
        not_found_error("Event", event_id)


    event.student_id = event_data.student_id
    event.title = event_data.title
    event.event_type = event_data.event_type
    event.event_date = event_data.event_date
    event.start_time = event_data.start_time
    event.end_time = event_data.end_time
    event.location = event_data.location


    db.commit()

    db.refresh(event)


    return event



# DELETE EVENT
@router.delete(
    "/{event_id}"
)
def delete_event(
    event_id: int,
    db: Session = Depends(get_db)
):

    event = (
        db.query(Event)
        .filter(Event.event_id == event_id)
        .first()
    )


    if not event:
        not_found_error("Event", event_id)


    db.delete(event)

    db.commit()


    return {
        "message": "Event deleted successfully"
    }