from fastapi import FastAPI
from contextlib import asynccontextmanager
from backend.src.database import create_tables, delete_tables
from backend.src.router import router as graves_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова к работе")
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan)
app.include_router(graves_router)



