from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from backend.home import router as home_router

app = FastAPI()

app.include_router(home_router)


@app.get("/")
def start():
    return RedirectResponse("/app")