from database import new_session, Tasks
from schemas import *
from sqlalchemy import select


class TasksRepository:
    @classmethod
    async def add_one(cls, data: TasksAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = Tasks(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            
            return task.id

    @classmethod
    async def get_all(cls):
        async with new_session() as session:
            query = select(Tasks)
            result = await session.execute(query)
            task_models = result.scalars().all()
            return task_models
        
    # @classmethod
    # async def get_all(cls) -> list[TasksRead]:
    #     async with new_session() as session:
    #         query = select(Tasks)
    #         result = await session.execute(query)
    #         task_models = result.scalars().all()
    #         task_schemas = [TasksRead.model_validate(tsk) for tsk in task_models]
    #         return task_schemas