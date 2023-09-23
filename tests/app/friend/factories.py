import factory
from pytest_factoryboy import register

from app.friend.models import Friend
from core.db import session
from tests.app.user.factories import UserModelFactory


@register
class FriendModelFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Friend
        sqlalchemy_session = session
        sqlalchemy_session_persistence = 'commit'

    initiator = factory.SubFactory(UserModelFactory)
    target = factory.SubFactory(UserModelFactory)
