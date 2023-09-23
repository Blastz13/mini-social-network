import pytest
import sqlalchemy

from app.chat.services import MessageService
from tests.app.user.conftest import user

@pytest.mark.parametrize('skip, limit, expected', [
    (0, 10, 10),
    (0, 5, 5),
    (0, 0, 0),
    pytest.param(-10, -1, 0, marks=pytest.mark.xfail(raises=sqlalchemy.exc.DataError)),
])
def test_get_message_list(message_list, skip, limit, expected):
    messages = MessageService().get_message_list(
        current_user_id=message_list[0].initiator.id,
        target_user_id=message_list[0].target.id,
        skip=skip,
        limit=limit,
    )
    assert len(messages) == expected


def test_create_message(user):
    message = MessageService().create_message(initiator_id=user.id, target_id=user.id, text='')
    assert message
