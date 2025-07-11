from asyncio import tasks
from fastapi import APIRouter, HTTPException
from models.task import Task
from data.db import tasks_db

router = APIRouter(prefix="/tasks", tags=["tasks"])

# Lire toutes les tâches
router.get('/')
def get_tasks():
    return tasks_db

#Lire une tâche par ID
@router.get("/{tasks_id}")
def get_task(tasks_id: int):
    for task in tasks_db:
        if task.task_id == tasks_id:
            return task
    raise HTTPException(status_code=404, detail="Tâche non trouvée")

#Créer une nouvelle tâche
@router.post("/")
def create_task(task: Task):
    tasks_db.append(task)
    return task

#Modifier une tâche existante
@router.put("/{tasks_id}")
def update_task(tasks_id: int, updated_task: Task):
    for i, task in enumerate(tasks_db):
        if task.task_id == tasks_id:
            tasks_db[i] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Tâche non trouvée")

#Supprimer une tâche
@router.delete("/{tasks_id}")
def delete_task(tasks_id: int):
    for task in tasks_db:
        if task.task_id == tasks_id:
            tasks_db.remove(task)
            return {"message": "Tâche supprimée"}
    raise HTTPException(status_code=404, detail="Tâche non trouvée")

