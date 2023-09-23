import pytest
import sqlalchemy

from app.friend.services import FriendService
from core.exceptions import NotFoundException


@pytest.mark.parametrize('skip, limit, expected', [
    (0, 10, 10),
    (0, 5, 5),
    (0, 0, 0),
    pytest.param(-10, -1, 0, marks=pytest.mark.xfail(raises=sqlalchemy.exc.DataError)),
])
def test_get_friend_list(friend_list, skip, limit, expected):
    friends = FriendService().get_friend_list(user_id=friend_list[0].initiator.id, skip=skip, limit=limit)
    assert len(friends) == expected


def test_remove_friend(friend):
    _friend = FriendService().remove_friend(id=friend.id)
    assert _friend == {}
    with pytest.raises(NotFoundException):
        _friend = FriendService().remove_friend(id=friend.id)
