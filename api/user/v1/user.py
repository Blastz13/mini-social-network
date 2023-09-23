
from fastapi import APIRouter, Query

from api.user.v1.request.user import LoginRequest
from api.user.v1.response.user import LoginResponse
from app.user.schemas import (
    CreateUserRequestSchema,
    CreateUserResponseSchema,
    ExceptionResponseSchema,
    GetRequestListResponseSchema,
)
from app.user.services import UserService

user_router = APIRouter()


@user_router.get(
    '',
    response_model=list[GetRequestListResponseSchema],
    response_model_exclude={'id'},
    responses={'400': {'model': ExceptionResponseSchema}},
    # dependencies=[Depends(PermissionDependency([IsAdmin]))],
)
def get_user_list(
    limit: int = Query(10, description='Limit'),
    skip: int = Query(None, description='Prev ID'),
):
    return UserService().get_user_list(limit=limit, skip=skip)


@user_router.post(
    '',
    response_model=CreateUserResponseSchema,
    responses={'400': {'model': ExceptionResponseSchema}},
)
def create_user(request: CreateUserRequestSchema):
    UserService().create_user(**request.dict())
    return {'email': request.email, 'nickname': request.nickname}


@user_router.post(
    '/login',
    response_model=LoginResponse,
    responses={'404': {'model': ExceptionResponseSchema}},
)
def login(request: LoginRequest):
    token = UserService().login(email=request.email, password=request.password)
    return {'token': token.token, 'refresh_token': token.refresh_token}
