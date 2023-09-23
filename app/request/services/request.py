
from sqlalchemy import or_, select, update

# from app.friend.services import FriendService
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
        pass

    def create_request(self, initiator_id: int, target_id: int) -> RequestFriend:
        pass

    def accept_request(self, id: int, user_id: int) -> RequestFriend:
        pass

    def get_request_or_404(cls, id: int) -> RequestFriend:
        pass

    def remove_request(self, user_id: int, id: int) -> dict:
        pass
