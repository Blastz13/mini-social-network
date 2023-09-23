from fastapi import APIRouter

from api.auth.auth import auth_router
from api.request.v1.request import request_router
from api.user.v1.user import user_router as user_v1_router

router = APIRouter()
router.include_router(user_v1_router, prefix='/api/v1/users', tags=['User'])
router.include_router(request_router, prefix='/api/v1/request', tags=['Request'])
router.include_router(auth_router, prefix='/auth', tags=['Auth'])


__all__ = ['router']
