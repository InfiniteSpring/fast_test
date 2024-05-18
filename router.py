from fastapi import APIRouter, Depends
from typing import Annotated
from schemas import *
from repository import TasksRepository


tasks_router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@tasks_router.get("")
# async def get_tasks() -> list[TasksRead]:
async def get_tasks():
    tasks = await TasksRepository.get_all()
    return tasks


@tasks_router.post("")
async def add_task(
    task: Annotated[TasksAdd, Depends()]
):
    task_id = await TasksRepository.add_one(task)
    return {
        "id_added": True,
        "task_id": task_id
    }