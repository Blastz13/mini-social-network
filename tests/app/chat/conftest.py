import pytest

from tests.app.chat.factories import MessageModelFactory
from tests.app.friend.factories import FriendModelFactory
from tests.app.user.factories import UserModelFactory


@pytest.fixture(scope='session')
def message_list():
    initiator = UserModelFactory()
    target = UserModelFactory()
    messages = MessageModelFactory.create_batch(10, initiator=initiator, target=target)
    yield messages
    # session.delete(user)
    # session.commit()


@pytest.fixture(scope='session')
def friend():
    friend = FriendModelFactory()
    yield friend
    # session.delete(user)
    # session.commit()
