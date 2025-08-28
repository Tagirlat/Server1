import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from starlette.middleware.cors import CORSMiddleware

from database import create_tables, delete_tables
from router import router as graves_router


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

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://www.kartapamyati.ru",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
    # uvicorn.run(app)



