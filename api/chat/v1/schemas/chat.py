from pydantic import BaseModel, Field


class GetMessageListResponseSchema(BaseModel):
    id: int = Field(..., description='ID')
    initiator_id: int = Field(..., description='initiator_id')
    target_id: int = Field(..., description='target_id')
    text: str = Field(..., description='text')

    class Config:
        orm_mode = True


class CreateMessageListRequestSchema(BaseModel):
    target_id: int = Field(..., description='target_id')
    text: str = Field(..., description='text')
