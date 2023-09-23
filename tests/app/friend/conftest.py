import pytest

from tests.app.friend.factories import FriendModelFactory
from tests.app.user.factories import UserModelFactory


@pytest.fixture(scope='session')
def friend_list():
    initiator = UserModelFactory()
    friends = FriendModelFactory.create_batch(10, initiator=initiator)
    yield friends
    # session.delete(user)
    # session.commit()


@pytest.fixture(scope='session')
def friend():
    friend = FriendModelFactory()
    yield friend
    # session.delete(user)
    # session.commit()
