from pydantic import BaseModel
from typing import Optional


class TasksAdd(BaseModel):
    name: str
    description: Optional[str] = None


class TasksRead(TasksAdd):
    id: int


# class TasksAddReturn(BaseModel):
#     is_created: bool = True
#     created_task_id: int