import pytest

from src.infra.db import engine
from src.infra.storage import EpisodeRepo


@pytest.fixture
def episode_repo():
    return EpisodeRepo(engine)
