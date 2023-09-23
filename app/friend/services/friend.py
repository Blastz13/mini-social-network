
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
        query = select(Friend).where(
            or_(
                Friend.target_id == user_id,
                Friend.initiator_id == user_id,
            ),
        )

        query = query.limit(limit).offset(skip).limit(limit)
        result = session.execute(query)
        return result.scalars().all()

    def create_friend(cls, initiator_id: int, target_id: int) -> Friend:
        friend = Friend(initiator_id=initiator_id, target_id=target_id)
        session.add(friend)
        session.commit()
        session.refresh(friend)
        return friend

    def get_friend_or_404(cls, id: int) -> Friend:
        result = session.execute(select(Friend).where(Friend.id == id))
        instance = result.scalar()
        if not instance:
            raise NotFoundException
        return instance

    def remove_friend(self, id: int) -> dict:
        friend = self.get_friend_or_404(id=id)
        session.delete(friend)
        session.commit()
        return {}
