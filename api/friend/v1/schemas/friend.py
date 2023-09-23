from pydantic import BaseModel, Field


class GetFriendListResponseSchema(BaseModel):
    id: int = Field(..., description='ID')
    initiator_id: int = Field(..., description='initiator_id')
    target_id: int = Field(..., description='target_id')

    class Config:
        orm_mode = True


class CreateFriendListRequestSchema(BaseModel):
    initiator_id: int = Field(..., description='initiator_id')
    target_id: int = Field(..., description='target_id')
