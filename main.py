from fastapi import FastAPI
import uvicorn

import dotenv
from aiomysql import create_pool
from contextlib import asynccontextmanager

from os import getenv

from routers import auth


dotenv.load_dotenv()


@asynccontextmanager
async def lifespan() -> None:
    app.state.pool = await create_pool(
        host=getenv("DB_HOST"),
        user=getenv("DB_USER"),
        password=getenv("DB_PASSWORD"),
        db=getenv("DB_NAME"),
    )
    yield
    app.state.pool.close()


app = FastAPI(liftspan=lifespan)
app.include_router(auth.router)


@app.get("/")
def main() -> str:
    return "Hello"


if __name__ == "__main__":
    uvicorn.run(app)