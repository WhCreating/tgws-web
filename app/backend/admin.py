from fastapi import Request
from fastapi.routing import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from logic.logic_tgws import get_proxy_url, TypeReturn

router = APIRouter()

templates = Jinja2Templates(directory="frontend")

@router.get("/admin")
async def admin(request: Request):
    return templates.TemplateResponse(request=request, name="admin_panel.html")