from sqlalchemy import BigInteger, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.user.models import User
from core.db import Base


class Friend(Base):
    __tablename__ = 'friends'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    initiator_id = Column(Integer, ForeignKey('users.id'))
    target_id = Column(Integer, ForeignKey('users.id'))
    initiator = relationship('User', backref='initiator_friend', primaryjoin=
                                                            initiator_id==User.id)
    target = relationship('User', backref='target_friend', primaryjoin=
                                                            target_id==User.id)
