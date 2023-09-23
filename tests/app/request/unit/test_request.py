import pytest
import sqlalchemy
from pytest_lazyfixture import lazy_fixture

from app.request.services import RequestService
from core.exceptions import NotFoundException
from tests.app.user.conftest import user


@pytest.mark.parametrize('skip, limit, expected', [
    (0, 10, 10),
    (0, 5, 5),
    (0, 0, 0),
    pytest.param(-10, -1, 0, marks=pytest.mark.xfail(raises=sqlalchemy.exc.DataError)),
])
def test_get_request_list(request_list_user, skip, limit, expected):
    requests = RequestService().get_request_list(user_id=request_list_user[0].initiator_id, skip=skip, limit=limit)
    assert len(requests) == expected


def test_create_request(user):
    request_friend = RequestService().create_request(initiator_id=user.id, target_id=user.id)
    assert request_friend


def test_accept_request(request_friend):
    _request = RequestService().accept_request(id=request_friend.id, user_id=request_friend.target_id)
    assert _request


@pytest.mark.parametrize('_request_friend', [
    pytest.param(lazy_fixture('request_friend')),
])
def test_remove_request(_request_friend):
    _request = RequestService().remove_request(id=_request_friend.id, user_id=_request_friend.target_id)
    assert _request == {}
    with pytest.raises(NotFoundException):
        _request = RequestService().remove_request(id=_request_friend.id, user_id=_request_friend.target_id)
