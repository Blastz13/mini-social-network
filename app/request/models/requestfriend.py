from sqlalchemy import BigInteger, Boolean, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.user.models import User
from core.db import Base


class RequestFriend(Base):
    __tablename__ = 'requests'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    initiator_id = Column(Integer, ForeignKey('users.id'))
    target_id = Column(Integer, ForeignKey('users.id'))
    status = Column(Boolean, default=False)
    initiator = relationship('User', backref='initiator', primaryjoin=
                                                            initiator_id==User.id)
    target = relationship('User', backref='target', primaryjoin=
                                                            target_id==User.id)
