from fastapi import APIRouter
from fastapi.requests import Request
from styler_utils.api.routers import ViewsetRouter

from .looks.views import LookViewset

viewset_router = ViewsetRouter()
viewset_router.include_viewset(LookViewset)

router = APIRouter(prefix="/api")

router.include_router(viewset_router, prefix="/looks")