
from sqlalchemy import or_, select, update

from app.friend.services import FriendService
from app.request.models import RequestFriend
from core.db import session
from core.exceptions import (
    NotFoundException,
)


class RequestService:
    def __init__(self):
        ...

    def get_request_list(
            self,
            user_id: int,
            limit: int = 12,
            skip: int = None,
    ) -> list[RequestFriend]:
        query = select(RequestFriend).where(
            or_(RequestFriend.initiator_id == user_id, RequestFriend.target_id == user_id),
        ).offset(
            skip,
        ).limit(limit)
        result = session.execute(query)
        return result.scalars().all()

    def create_request(self, initiator_id: int, target_id: int) -> RequestFriend:
        request = RequestFriend(initiator_id=initiator_id, target_id=target_id)
        session.add(request)
        session.commit()
        return request

    def accept_request(self, id: int, user_id: int) -> RequestFriend:
        request = self.get_request_or_404(id=id)
        query = (
            update(RequestFriend)
            .where(RequestFriend.id == id, RequestFriend.target_id == user_id)
            .values(status=True)
            .execution_options(synchronize_session='fetch')
        )
        session.execute(query)
        session.commit()
        FriendService().create_friend(initiator_id=request.initiator_id, target_id=request.target_id)
        return request

    def get_request_or_404(cls, id: int) -> RequestFriend:
        result = session.execute(select(RequestFriend).where(RequestFriend.id == id))
        instance = result.scalar()
        if not instance:
            raise NotFoundException
        return instance

    def remove_request(self, user_id: int, id: int) -> dict:
        request = self.get_request_or_404(id=id)
        if request.target_id == user_id or request.initiator_id == user_id:
            session.delete(request)
            session.commit()
            return {}
        else:
            raise NotFoundException
