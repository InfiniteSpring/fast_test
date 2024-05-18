from pydantic import BaseModel
from typing import Optional
from pydantic import ConfigDict


class TasksAdd(BaseModel):
    name: str
    description: Optional[str] = None


class TasksRead(TasksAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


# class TasksAddReturn(BaseModel):
#     is_created: bool = True
#     created_task_id: int

    # model_config = ConfigDict(from_attributes=True)