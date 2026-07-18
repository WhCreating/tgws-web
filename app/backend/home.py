from fastapi import Request
from fastapi.routing import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

router = APIRouter()

templates = Jinja2Templates(directory="frontend")

@router.get("/")
async def home():
    return {
        "msg": "Hello"
    }