
from fastapi import APIRouter, Depends, Query, Request

from api.chat.v1.schemas.chat import CreateMessageListRequestSchema, GetMessageListResponseSchema
from app.chat.services import MessageService
from app.user.schemas import ExceptionResponseSchema
from core.fastapi.dependencies import (
    IsAuthenticated,
    PermissionDependency,
)

chat_router = APIRouter()


@chat_router.get(
    '/{id}',
    response_model=list[GetMessageListResponseSchema],
    responses={'400': {'model': ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
)
def get_message_list(
        id: int,
        request: Request,
        limit: int = Query(10, description='Limit'),
        skip: int = Query(None, description='Prev ID'),
):
    return MessageService().get_message_list(current_user_id=request.user.id, target_user_id=id, skip=skip, limit=limit)


@chat_router.post(
    '/{id}',
    status_code=201,
    response_model=GetMessageListResponseSchema,
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
)
def create_message(request: Request, message: CreateMessageListRequestSchema):
    return MessageService().create_message(initiator_id=request.user.id, **message.dict())
