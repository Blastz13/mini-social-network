import factory
from pytest_factoryboy import register

from app.user.models import User
from core.db import session


@register
class UserModelFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = session
        sqlalchemy_session_persistence = 'commit'

    password = factory.Faker('name')
    email = factory.Faker('email')
    nickname = factory.Faker('name')
    is_admin = False
