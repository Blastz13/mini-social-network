
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
        query = select(User).offset(skip).limit(limit)
        result = session.execute(query)
        return result.scalars().all()

    def create_user(
        self, email: str, password1: str, password2: str, nickname: str,
    ) -> User:
        if password1 != password2:
            raise PasswordDoesNotMatchException

        query = select(User).where(or_(User.email == email, User.nickname == nickname))
        result = session.execute(query)
        is_exist = result.scalars().first()
        if is_exist:
            raise DuplicateEmailOrNicknameException

        user = User(email=email, password=password1, nickname=nickname)
        session.add(user)
        session.commit()
        return user

    def is_admin(self, user_id: int) -> bool:
        result = session.execute(select(User).where(User.id == user_id))
        user = result.scalars().first()
        if not user:
            return False

        if user.is_admin is False:
            return False

        return True

    def login(self, email: str, password: str) -> LoginResponseSchema:
        result = session.execute(
            select(User).where(and_(User.email == email, password == password)),
        )
        user = result.scalars().first()
        if not user:
            raise UserNotFoundException

        response = LoginResponseSchema(
            token=TokenHelper.encode(payload={'user_id': user.id}),
            refresh_token=TokenHelper.encode(payload={'sub': 'refresh'}),
        )
        return response
