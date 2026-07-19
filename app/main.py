from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from backend.routers import router as app_router

app = FastAPI()

app.include_router(app_router)