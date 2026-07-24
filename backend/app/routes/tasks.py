from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import Query
from app.schemas.pagination import PaginationResponse
from app.database.dependency import get_db
from app.models import Task
from app.schemas.task import TaskCreate, TaskResponse
from app.core.exceptions import not_found_error

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get("/", response_model=PaginationResponse[TaskResponse])
def get_tasks(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):

    skip = (page - 1) * limit

    total = db.query(Task).count()

    tasks = (
        db.query(Task)
        .offset(skip)
        .limit(limit)
        .all()
    )

    return PaginationResponse(
        total=total,
        page=page,
        limit=limit,
        data=tasks
    )



@router.post("/", response_model=TaskResponse)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db)
):

    new_task = Task(
        title=task.title,
        priority=task.priority,
        status=task.status,
        due_date=task.due_date,
        student_id=4
    )

    db.add(new_task)

    db.commit()

    db.refresh(new_task)

    return new_task

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task: TaskCreate,
    db: Session = Depends(get_db)
):

    existing_task = (
        db.query(Task)
        .filter(Task.task_id == task_id)
        .first()
    )

    if not existing_task:
        not_found_error("Task", task_id)

    existing_task.title = task.title
    existing_task.priority = task.priority
    existing_task.status = task.status
    existing_task.due_date = task.due_date

    db.commit()

    db.refresh(existing_task)

    return existing_task

@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):

    task = (
        db.query(Task)
        .filter(Task.task_id == task_id)
        .first()
    )

    if not task:
        not_found_error(
            "Task",
            task_id
        )

    db.delete(task)

    db.commit()

    return {
        "message": "Task deleted successfully"
    }




