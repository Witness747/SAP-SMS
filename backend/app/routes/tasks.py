from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependency import get_db
from app.models import Task
from app.schemas.task import TaskCreate, TaskResponse


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get("/", response_model=list[TaskResponse])
def get_tasks(
    db: Session = Depends(get_db)
):

    tasks = db.query(Task).all()

    return tasks



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
        return {
            "message": "Task not found"
        }

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
        return {
            "message": "Task not found"
        }

    db.delete(task)

    db.commit()

    return {
        "message": "Task deleted successfully"
    }




