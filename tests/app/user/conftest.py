import pytest

from tests.app.user.factories import UserModelFactory


@pytest.fixture(scope='session')
def user_list():
    user = UserModelFactory.create_batch(10)
    yield user
    # session.delete(user)
    # session.commit()


@pytest.fixture(scope='session')
def user():
    user = UserModelFactory()
    yield user
    # session.delete(user)
    # session.commit()
