import pytest
from uuid import UUID

from src.infra.storage import EpisodeRepo
from src.api.interactor import ApiInteractor
from src.domain.episode import Episode

episode_repo = EpisodeRepo()

MOCK_EPISODE = {
    "id": "9b81efb6-e8a1-11ec-9e1d-eb36b3ac7ec2",
    "episodeTitle": "Economics 101",
    "podcastTitle": "Money and Fame",
    "thumbnailUrl": "https://example.com/somethumbnail.png",
    "guests": [{"name": "Adam Smith"}, {"name": "Karl Marx"}],
    "audioUrl": "https://example.com/episode_economics_101.mp3",
    "episodeDurationSeconds": 2100,
}


@pytest.fixture
def mock_read_episode_response(monkeypatch):
    """Provide the mock response of read_episode methods (of EpisodeRepo class)"""

    def mock_read_episode(id: UUID):
        if id == UUID(MOCK_EPISODE["id"]):
            return Episode(**MOCK_EPISODE)
        else:
            return None

    monkeypatch.setattr(episode_repo, "read_episode", mock_read_episode)


@pytest.fixture
def mock_delete_episode_response(monkeypatch):
    """Provide the mock response of delete_episode methods (of EpisodeRepo classs)"""

    def mock_delete_episode(id: UUID):
        if id == UUID(MOCK_EPISODE["id"]):
            return "Success"
        else:
            return "Fail"

    monkeypatch.setattr(episode_repo, "delete_episode", mock_delete_episode)


@pytest.fixture
def api_interactor(mock_read_episode_response, mock_delete_episode_response):
    return ApiInteractor(episode_repo)
