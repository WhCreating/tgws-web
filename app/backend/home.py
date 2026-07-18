from fastapi import Request
from fastapi.routing import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from logic.logic_tgws import get_proxy_url, TypeReturn

router = APIRouter()

templates = Jinja2Templates(directory="frontend")

@router.get("/")
async def home(request: Request):
    url = get_proxy_url()
    server = get_proxy_url(TypeReturn.SERVER)
    port = get_proxy_url(TypeReturn.PORT)
    secret = get_proxy_url(TypeReturn.SECRET)

    return templates.TemplateResponse(
        request=request, name="url_telegram.html", context={
            "url_proxy": url,
            "server": server,
            "port": port,
            "secret": secret
        }
    )