from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependency import get_db
from app.models import Course
from app.schemas.course import CourseCreate, CourseResponse


router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)


@router.get("/", response_model=list[CourseResponse])
def get_courses(
    db: Session = Depends(get_db)
):

    courses = db.query(Course).all()

    return courses



@router.post("/", response_model=CourseResponse)
def create_course(
    course: CourseCreate,
    db: Session = Depends(get_db)
):

    new_course = Course(
        course_name=course.course_name,
        course_code=course.course_code,
        semester=course.semester,
        student_id=4
    )

    db.add(new_course)

    db.commit()

    db.refresh(new_course)

    return new_course

@router.put("/{course_id}", response_model=CourseResponse)
def update_course(
    course_id: int,
    course: CourseCreate,
    db: Session = Depends(get_db)
):

    existing_course = (
        db.query(Course)
        .filter(Course.course_id == course_id)
        .first()
    )

    if not existing_course:
        return {
            "message": "Course not found"
        }

    existing_course.course_name = course.course_name
    existing_course.course_code = course.course_code
    existing_course.semester = course.semester

    db.commit()

    db.refresh(existing_course)

    return existing_course

@router.delete("/{course_id}")
def delete_course(
    course_id: int,
    db: Session = Depends(get_db)
):

    course = (
        db.query(Course)
        .filter(Course.course_id == course_id)
        .first()
    )

    if not course:
        return {
            "message": "Course not found"
        }

    db.delete(course)

    db.commit()

    return {
        "message": "Course deleted successfully"
    }