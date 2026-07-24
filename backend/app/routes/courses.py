from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import Query
from app.schemas.pagination import PaginationResponse
from app.database.dependency import get_db
from app.models import Course
from app.schemas.course import CourseCreate, CourseResponse
from app.core.exceptions import not_found_error

router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)


@router.get("/", response_model=PaginationResponse[CourseResponse])
def get_courses(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):

    skip = (page - 1) * limit

    total = db.query(Course).count()

    courses = (
        db.query(Course)
        .offset(skip)
        .limit(limit)
        .all()
    )

    return PaginationResponse(
        total=total,
        page=page,
        limit=limit,
        data=courses
    )



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
        not_found_error("Course", course_id)

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
        not_found_error("Course", course_id)

    db.delete(course)

    db.commit()

    return {
        "message": "Course deleted successfully"
    }