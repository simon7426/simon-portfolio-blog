from fastapi import APIRouter

from project.apis.alive import router as alive_router
from project.apis.auth.views import router as users_router
from project.apis.blogs.views import router as blogs_router

router = APIRouter()

router.include_router(alive_router)
router.include_router(users_router)
router.include_router(blogs_router)
