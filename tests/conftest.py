import pytest

from core.db import Base
from core.db.session import engine, session


@pytest.fixture(scope='session', autouse=True)
def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


@pytest.fixture(scope='function', autouse=True)
def _session():
    session.begin_nested()
    yield session
    session.rollback()
