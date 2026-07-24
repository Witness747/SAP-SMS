from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import Query
from app.database.dependency import get_db
from app.models import Student
from app.schemas.student import StudentCreate, StudentResponse
from app.core.exceptions import not_found_error
from app.schemas.pagination import PaginationResponse

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.get("/", response_model=PaginationResponse[StudentResponse])
def get_students(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):

    skip = (page - 1) * limit

    total = db.query(Student).count()

    students = (
        db.query(Student)
        .offset(skip)
        .limit(limit)
        .all()
    )

    return PaginationResponse(
        total=total,
        page=page,
        limit=limit,
        data=students
    )



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
        not_found_error("Student", student_id)

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
        not_found_error("Student", student_id)

    db.delete(student)

    db.commit()

    return {
        "message": "Student deleted successfully"
    }
