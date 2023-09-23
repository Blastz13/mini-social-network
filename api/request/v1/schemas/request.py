from pydantic import BaseModel, Field


class GetRequestListResponseSchema(BaseModel):
    id: int = Field(..., description='ID')
    initiator_id: int = Field(..., description='initiator_id')
    target_id: int = Field(..., description='target_id')
    status: bool = Field(..., description='status')

    class Config:
        orm_mode = True


class CreateRequestListRequestSchema(BaseModel):
    target_id: int = Field(..., description='target_id')
