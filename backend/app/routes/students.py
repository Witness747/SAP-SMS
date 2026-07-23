from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependency import get_db
from app.models import Student


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.get("/")
def get_students(
    db: Session = Depends(get_db)
):

    students = db.query(Student).all()

    return students