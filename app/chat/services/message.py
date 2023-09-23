
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
        pass

    def create_message(
            self, initiator_id: int, target_id: int, text: str,
    ) -> Message:
        pass
