from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependency import get_db
from app.models import Student
from app.schemas.student import StudentCreate, StudentResponse


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.get("/", response_model=list[StudentResponse])
def get_students(
    db: Session = Depends(get_db)
):

    students = db.query(Student).all()

    return students



@router.post("/", response_model=StudentResponse)
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):

    new_student = Student(
        full_name=student.full_name,
        email=student.email,
        program=student.program
    )

    db.add(new_student)

    db.commit()

    db.refresh(new_student)

    return new_student

@router.put("/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int,
    student: StudentCreate,
    db: Session = Depends(get_db)
):

    existing_student = (
        db.query(Student)
        .filter(Student.student_id == student_id)
        .first()
    )

    if not existing_student:
        return {
            "message": "Student not found"
        }

    existing_student.full_name = student.full_name
    existing_student.email = student.email
    existing_student.program = student.program

    db.commit()

    db.refresh(existing_student)

    return existing_student

@router.delete("/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = (
        db.query(Student)
        .filter(Student.student_id == student_id)
        .first()
    )

    if not student:
        return {
            "message": "Student not found"
        }

    db.delete(student)

    db.commit()

    return {
        "message": "Student deleted successfully"
    }
