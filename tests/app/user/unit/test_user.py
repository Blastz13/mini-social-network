import pytest
import sqlalchemy

from app.user.services import UserService
from core.exceptions import DuplicateEmailOrNicknameException, PasswordDoesNotMatchException, UserNotFoundException


@pytest.mark.parametrize('skip, limit, expected', [
    (0, 10, 10),
    (0, 5, 5),
    (0, 0, 0),
    pytest.param(-10, -1, 0, marks=pytest.mark.xfail(raises=sqlalchemy.exc.DataError)),
])
def test_get_user_list(user_list, skip, limit, expected):
    users = UserService().get_user_list(skip=skip, limit=limit)
    assert len(users) == expected


@pytest.mark.parametrize('email, password1, password2, nickname', [
    ('test@mail.ru', 'pass1', 'pass1', 'nick'),
    pytest.param('test@mail.ru', 'pass1', 'pass1', 'nick',
                 marks=pytest.mark.xfail(raises=DuplicateEmailOrNicknameException)),
    pytest.param('test@mail.ru', 'pass1', 'pass2', 'nick',
                 marks=pytest.mark.xfail(raises=PasswordDoesNotMatchException)),
])
def test_create_user(email, password1, password2, nickname):
    user = UserService().create_user(email=email, password1=password1, password2=password2, nickname=nickname)
    assert user


@pytest.mark.parametrize('email, password', [
    pytest.param('test@mail.ru', 'pass',
                 marks=pytest.mark.xfail(raises=UserNotFoundException)),
])
def test_login_user(email, password):
    user = UserService().login(email=email, password=password)
    assert user
