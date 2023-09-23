
from sqlalchemy import and_, or_, select

from app.chat.models import Message
from core.db import session


class MessageService:
    def __init__(self):
        ...

    def get_message_list(
            self,
            current_user_id: int,
            target_user_id: int,
            skip: int,
            limit: int,

    ) -> list[Message]:
        query = select(Message).where(
            or_(
                and_(Message.target_id == current_user_id, Message.initiator_id == target_user_id),
                and_(Message.target_id == target_user_id, Message.initiator_id == current_user_id),
            ),
        ).offset(
            skip,
        ).limit(limit)
        result = session.execute(query)
        return result.scalars().all()

    def create_message(
            self, initiator_id: int, target_id: int, text: str,
    ) -> Message:
        message = Message(initiator_id=initiator_id, target_id=target_id, text=text)
        session.add(message)
        session.commit()
        return message
