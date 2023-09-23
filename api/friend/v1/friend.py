
from fastapi import APIRouter, Depends, Query, Request

from api.friend.v1.schemas.friend import GetFriendListResponseSchema
from app.friend.services import FriendService
from app.user.schemas import ExceptionResponseSchema
from core.fastapi.dependencies import (
    IsAuthenticated,
    PermissionDependency,
)

friend_router = APIRouter()


@friend_router.get(
    '',
    response_model=list[GetFriendListResponseSchema],
    responses={'400': {'model': ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
)
def get_friend_list(
        request: Request,
        limit: int = Query(10, description='Limit'),
        skip: int = Query(None, description='Prev ID'),
):
    return FriendService().get_friend_list(request.user.id, limit=limit, skip=skip)


@friend_router.delete(
    '/{id}',
    status_code=204,
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
)
def delete_friend(id: int):
    return FriendService().remove_friend(id)
