
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from core.config import config

DATABASE_URL = config.WRITER_DB_URL

engine = create_engine(DATABASE_URL)
session = scoped_session(
    sessionmaker(
        autocommit=False,
        bind=engine,
    ),
)
Base = declarative_base()


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
