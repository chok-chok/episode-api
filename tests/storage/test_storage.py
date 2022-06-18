import pytest

from uuid import uuid4
from src.infra.storage import EpisodeRepo


# Tests for read_episode method


def test_read_episode_success(episode_repo: EpisodeRepo, test_dataset):
    """Should return correct instance of episode"""
    """TODO: Parameterize the test"""
    assert episode_repo.read_episode(test_dataset[0]["id"]) == test_dataset[0]
    assert episode_repo.read_episode(test_dataset[99]["id"]) == test_dataset[99]
    assert episode_repo.read_episode(test_dataset[80]["id"]) == test_dataset[80]


def test_read_episode_null_case(episode_repo: EpisodeRepo, test_dataset):
    """Should return None"""
    assert episode_repo.read_episode(uuid4()) == None


# Tests for read_episodes method


def test_read_episodes_success(episode_repo: EpisodeRepo, test_dataset):
    result = episode_repo.read_episodes()

    assert (len(result)) == len(test_dataset)
    assert episode_repo.read_episode(test_dataset[0]["id"]) == test_dataset[0]
    assert episode_repo.read_episode(test_dataset[99]["id"]) == test_dataset[99]
    assert episode_repo.read_episode(test_dataset[80]["id"]) == test_dataset[80]


# Tests for create_episode method


def test_create_episode_success(episode_repo: EpisodeRepo, test_dataset):
    CREATE_EPISODE_INPUT = dict(
        episodeTitle="Debt based monetary system",
        podcastTitle="Money and Fame",
        thumbnailUrl="https://example.com/somethumbnail_2.png",
        guests=[dict(name="John Maynard Keynes")],
        audioUrl="https://example.com/episode_currency_and_money.mp3",
        episodeDurationSeconds=3000,
    )

    result = episode_repo.create_episode(CREATE_EPISODE_INPUT)

    assert result.episodeTitle == CREATE_EPISODE_INPUT["episodeTitle"]
    assert result.podcastTitle == CREATE_EPISODE_INPUT["podcastTitle"]
    assert result.thumbnailUrl == CREATE_EPISODE_INPUT["thumbnailUrl"]
    assert result.guests == CREATE_EPISODE_INPUT["guests"]
    assert result.audioUrl == CREATE_EPISODE_INPUT["audioUrl"]
    assert (
        result.episodeDurationSeconds == CREATE_EPISODE_INPUT["episodeDurationSeconds"]
    )
