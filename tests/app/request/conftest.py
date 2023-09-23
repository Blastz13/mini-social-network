import pytest

from tests.app.request.factories import RequestModelFactory
from tests.app.user.factories import UserModelFactory


@pytest.fixture(scope='session')
def request_list():
    requests = RequestModelFactory.create_batch(10)
    yield requests
    # session.delete(user)
    # session.commit()


@pytest.fixture(scope='session')
def request_friend():
    request = RequestModelFactory()
    yield request
    # session.delete(user)
    # session.commit()


@pytest.fixture(scope='session')
def request_list_user():
    initiator = UserModelFactory()
    requests = RequestModelFactory.create_batch(10, initiator=initiator)
    yield requests
    # session.delete(user)
    # session.commit()
