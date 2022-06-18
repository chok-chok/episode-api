import pytest

from src.infra.storage import EpisodeRepo


def test_example(episode_repo: EpisodeRepo, test_dataset):
    assert len(test_dataset) == 100
