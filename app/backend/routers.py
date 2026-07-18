from fastapi import Request
from fastapi.routing import APIRouter
from fastapi.staticfiles import StaticFiles

from backend.home import router as home_router
from backend.admin import router as admin_router

router = APIRouter()
router.mount("/app", StaticFiles(directory="frontend/static"), name="static")


router.include_router(home_router)
router.include_router(admin_router)
