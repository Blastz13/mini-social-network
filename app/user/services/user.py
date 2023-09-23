
from sqlalchemy import and_, or_, select

from app.user.models import User
from app.user.schemas.user import LoginResponseSchema
from core.db import session
from core.exceptions import (
    DuplicateEmailOrNicknameException,
    PasswordDoesNotMatchException,
    UserNotFoundException,
)
from core.utils.token_helper import TokenHelper


class UserService:
    def __init__(self):
        ...

    def get_user_list(
        self,
        skip: int,
        limit: int = 12,
    ) -> list[User]:
        pass

    def create_user(
        self, email: str, password1: str, password2: str, nickname: str,
    ) -> User:
        pass

    def is_admin(self, user_id: int) -> bool:
        pass

    def login(self, email: str, password: str) -> LoginResponseSchema:
        pass
