import pytest

from src.infra.storage import EpisodeRepo


def test_example(episode_repo: EpisodeRepo):
    assert 1 == 1
