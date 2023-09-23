from sqlalchemy import BigInteger, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.user.models import User
from core.db import Base


class Message(Base):
    __tablename__ = 'messages'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    initiator_id = Column(Integer, ForeignKey('users.id'))
    target_id = Column(Integer, ForeignKey('users.id'))
    text = Column(String)
    initiator = relationship('User', backref='initiator_message', primaryjoin=
                                                            initiator_id==User.id)
    target = relationship('User', backref='target_message', primaryjoin=
                                                            target_id==User.id)
