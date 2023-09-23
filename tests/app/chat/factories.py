import factory
from pytest_factoryboy import register

from app.chat.models import Message
from core.db import session
from tests.app.user.factories import UserModelFactory


@register
class MessageModelFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Message
        sqlalchemy_session = session
        sqlalchemy_session_persistence = 'commit'

    initiator = factory.SubFactory(UserModelFactory)
    target = factory.SubFactory(UserModelFactory)
    text = factory.Faker('name')
