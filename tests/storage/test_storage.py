import pytest

from uuid import uuid4
from src.infra.storage import EpisodeRepo


def test_example(episode_repo: EpisodeRepo, test_dataset):
    assert len(test_dataset) == 100


def test_read_episode_success(episode_repo: EpisodeRepo, test_dataset):
    """Should return correct instance of episode"""
    """TODO: Parameterize the test"""
    assert episode_repo.read_episode(test_dataset[0]["id"]) == test_dataset[0]
    assert episode_repo.read_episode(test_dataset[99]["id"]) == test_dataset[99]
    assert episode_repo.read_episode(test_dataset[80]["id"]) == test_dataset[80]


def test_read_episode_null_case(episode_repo: EpisodeRepo, test_dataset):
    """Should return None"""
    assert episode_repo.read_episode(uuid4()) == None
