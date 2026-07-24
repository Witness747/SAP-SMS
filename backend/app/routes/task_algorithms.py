# DSA Algorithms Endpoints
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from app.database.dependency import get_db
from app.models import Task
from app.schemas.task import TaskCreate, TaskResponse
from app.schemas.task_algorithms import (
    TaskAlgorithmResponse,
    TaskSearchResponse,
    TaskPriorityResponse
)
from app.services.task_algorithms import (
    sort_tasks_by_deadline,
    search_tasks_by_title,
    sort_tasks_by_priority
)

router = APIRouter(
    prefix="/tasks",
    tags=["Task Algorithms"]
)
# 1 Sorting by Deadline
@router.get(
    "/sorted/deadline",
    response_model=list[TaskAlgorithmResponse]
)
def get_tasks_sorted_by_deadline(
    db: Session = Depends(get_db)
):

    tasks = db.query(Task).all()

    sorted_tasks = sort_tasks_by_deadline(tasks)

    return sorted_tasks

# 2 Searching by Title
@router.get(
    "/search/{keyword}",
    response_model=list[TaskSearchResponse]
)
def search_tasks(
    keyword: str,
    db: Session = Depends(get_db)
):

    tasks = db.query(Task).all()

    results = search_tasks_by_title(
        tasks,
        keyword
    )

    return results

#3 Sorting by Priority
@router.get(
    "/sorted/priority",
    response_model=list[TaskPriorityResponse]
)
def get_tasks_sorted_by_priority(
    db: Session = Depends(get_db)
):

    tasks = db.query(Task).all()

    sorted_tasks = sort_tasks_by_priority(tasks)

    return sorted_tasks

