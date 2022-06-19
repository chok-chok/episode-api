import pytest

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database, drop_database

from src.infra.db import engine
from src.infra.models import episode_schema
from src.infra.storage import EpisodeRepo

from src.config import DB_HOST, DB_USER, DB_PWD
from .helpers import generate_test_dataset


@pytest.fixture
def test_dataset():
    return generate_test_dataset()


@pytest.fixture
def test_db_session(test_dataset):

    engine = create_engine(f"postgresql://{DB_USER}:{DB_PWD}@{DB_HOST}:5432/testdb")

    # Create a test database
    if not database_exists(engine.url):
        create_database(engine.url)

    # Create a new episode table
    episode_schema.create(engine, checkfirst=True)

    # Insert the test dataset to test database
    engine.execute(episode_schema.insert(), test_dataset)

    yield engine

    # Start teardown process

    # First, drop the episode table
    episode_schema.drop(engine, checkfirst=True)

    # Second, drop the test database
    drop_database(engine.url)


@pytest.fixture()
def episode_repo(test_db_session, test_dataset):
    from src.infra.models import episode_schema

    return EpisodeRepo(test_db_session, episode_schema)
