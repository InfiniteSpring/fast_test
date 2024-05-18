from fastapi import FastAPI

from contextlib import asynccontextmanager
from database import create_all_tables, delete_all_tables

from router import tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # try:
    #     await delete_all_tables()
    #     await create_all_tables()
    #     print("Base in default state now.\nBase ready to be changed")
    # except:
    #     print("Some error in clean up all changes is db")

    yield 
    print("Reboot is complite.")
 
 
app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)

