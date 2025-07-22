from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/tasks", tags=["Tasks"])

class Task(BaseModel):
    id: int
    title: str
    completed: bool
    assigned_to: str

# Dummy in-memory store
tasks_db: List[Task] = []

@router.get("/", response_model=List[Task])
def get_tasks():
    return tasks_db

@router.post("/")
def create_task(task: Task):
    tasks_db.append(task)
    return {"status": "created", "task": task}

@router.patch("/{task_id}")
def toggle_task(task_id: int):
    for task in tasks_db:
        if task.id == task_id:
            task.completed = not task.completed
            return {"status": "updated", "task": task}
    return {"error": "Task not found"}

@router.delete("/{task_id}")
def delete_task(task_id: int):
    global tasks_db
    tasks_db = [t for t in tasks_db if t.id != task_id]
    return {"status": "deleted"}