from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependency import get_db
from app.models import Event
from app.schemas.event import EventCreate, EventResponse


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
    response_model=list[EventResponse]
)
def get_events(
    db: Session = Depends(get_db)
):

    events = db.query(Event).all()

    return events



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
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )


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
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )


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
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )


    db.delete(event)

    db.commit()


    return {
        "message": "Event deleted successfully"
    }