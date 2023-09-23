import os

from dotenv import find_dotenv, load_dotenv
from pydantic import BaseSettings

load_dotenv(find_dotenv())


class Config(BaseSettings):
    ENV: str = 'development'
    DEBUG: bool = True
    APP_HOST: str = '0.0.0.0'
    APP_PORT: int = 8000
    WRITER_DB_URL: str = f"postgresql://{os.getenv('POSTGRES_USER')}:" \
                         f"{os.getenv('POSTGRES_PASSWORD')}@" \
                         f"{os.getenv('POSTGRES_HOST')}:" \
                         f"{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
    READER_DB_URL: str = 'mysql+aiomysql://fastapi:fastapi@localhost:3306/fastapi'
    JWT_SECRET_KEY: str = 'fastapi'
    JWT_ALGORITHM: str = 'HS256'
    SENTRY_SDN: str = None
    CELERY_BROKER_URL: str = 'amqp://user:bitnami@localhost:5672/'
    CELERY_BACKEND_URL: str = 'redis://:password123@localhost:6379/0'
    REDIS_HOST: str = 'localhost'
    REDIS_PORT: int = 6379


class DevelopmentConfig(Config):
    WRITER_DB_URL: str = f"postgresql://{os.getenv('POSTGRES_USER')}:" \
                         f"{os.getenv('POSTGRES_PASSWORD')}@" \
                         f"{os.getenv('POSTGRES_HOST')}:" \
                         f"{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
    READER_DB_URL: str = f"postgresql://{os.getenv('POSTGRES_USER')}:" \
                         f"{os.getenv('POSTGRES_PASSWORD')}@" \
                         f"{os.getenv('POSTGRES_HOST')}:" \
                         f"{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"


class LocalConfig(Config):
    WRITER_DB_URL: str = f"postgresql://{os.getenv('POSTGRES_USER')}:" \
                         f"{os.getenv('POSTGRES_PASSWORD')}@" \
                         f"{os.getenv('POSTGRES_HOST')}:" \
                         f"{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
    READER_DB_URL: str = 'mysql+aiomysql://fastapi:fastapi@localhost:3306/fastapi'


class ProductionConfig(Config):
    DEBUG: str = False
    WRITER_DB_URL: str = 'mysql+aiomysql://fastapi:fastapi@localhost:3306/prod'
    READER_DB_URL: str = 'mysql+aiomysql://fastapi:fastapi@localhost:3306/prod'


def get_config():
    env = os.getenv('ENV', 'local')
    config_type = {
        'dev': DevelopmentConfig(),
        'local': LocalConfig(),
        'prod': ProductionConfig(),
    }
    return config_type[env]


config: Config = get_config()
print(config.WRITER_DB_URL)
