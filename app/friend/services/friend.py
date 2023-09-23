
from sqlalchemy import or_, select

from app.friend.models import Friend
from core.db import session
from core.exceptions import NotFoundException


class FriendService:
    def __init__(self):
        ...

    def get_friend_list(
            self,
            user_id: int,
            skip: int,
            limit: int = 12,
    ) -> list[Friend]:
        pass

    def create_friend(cls, initiator_id: int, target_id: int) -> Friend:
        pass

    def get_friend_or_404(cls, id: int) -> Friend:
        pass

    def remove_friend(self, id: int) -> dict:
        pass
