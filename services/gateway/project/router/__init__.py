from fastapi import APIRouter

from .admin import router as admin_router
from .alive import router as alive_router
from .client import router as client_router

router = APIRouter()

router.include_router(alive_router)
router.include_router(client_router)
router.include_router(admin_router)
