from fastapi import FastAPI
from backend.home import router as home_router

app = FastAPI()

app.include_router(home_router)