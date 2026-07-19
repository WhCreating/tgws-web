from fastapi import Request
from fastapi.routing import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, Response

from logic.logic_tgws import restart_tgws

router = APIRouter()

templates = Jinja2Templates(directory="frontend")

@router.get("/admin")
async def admin(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="admin_panel.html"
    )

@router.post("/restart-proxy/{password}")
async def restart_proxy(password: str):
    res = restart_tgws(password)
    print(res)
    if res:
        return Response(status_code=200)
    else :
        return Response(status_code=401)