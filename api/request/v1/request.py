
from fastapi import APIRouter, Depends, Query, Request

from api.request.v1.schemas.request import CreateRequestListRequestSchema, GetRequestListResponseSchema
from app.request.services import RequestService
from app.user.schemas import ExceptionResponseSchema
from core.fastapi.dependencies import (
    IsAuthenticated,
    PermissionDependency,
)

request_router = APIRouter()


@request_router.get(
    '',
    response_model=list[GetRequestListResponseSchema],
    responses={'400': {'model': ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
)
def get_request_list(
        request: Request,
        limit: int = Query(10, description='Limit'),
        skip: int = Query(None, description='Prev ID'),
):
    return RequestService().get_request_list(user_id=request.user.id, limit=limit, skip=skip)


@request_router.post(
    '',
    response_model=GetRequestListResponseSchema,
    responses={'400': {'model': ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
)
def create_request(request: Request, _request: CreateRequestListRequestSchema):
    return RequestService().create_request(initiator_id=request.user.id, **_request.dict())


@request_router.put(
    '/{id}',
    response_model=GetRequestListResponseSchema,
    responses={'400': {'model': ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
)
def accept_request(request: Request, id: int):
    return RequestService().accept_request(id=id, user_id=request.user.id)


@request_router.delete(
    '/{id}',
    status_code=204,
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
)
def remove_request(request: Request, id: int):
    return RequestService().remove_request(user_id=request.user.id, id=id)
