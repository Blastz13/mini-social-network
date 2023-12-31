from sqlalchemy import BigInteger, Boolean, Column, String

from core.db import Base
from core.db.mixins import TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    password = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    nickname = Column(String(255), nullable=False, unique=True)
    is_admin = Column(Boolean, default=False)
