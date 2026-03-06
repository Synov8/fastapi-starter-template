from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware


from fastapi import FastAPI
from app.config import settings
from app.routers import routers

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Before
    yield
    # After


app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.app_url],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for router in routers:
    app.include_router(router)
