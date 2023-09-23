import factory
from pytest_factoryboy import register

from app.request.models import RequestFriend
from core.db import session
from tests.app.user.factories import UserModelFactory


@register
class RequestModelFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = RequestFriend
        sqlalchemy_session = session
        sqlalchemy_session_persistence = 'commit'

    initiator = factory.SubFactory(UserModelFactory)
    target = factory.SubFactory(UserModelFactory)
    status = False
