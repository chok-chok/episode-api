import pytest
from uuid import UUID, uuid4

from src.infra.db import engine
from src.infra.storage import EpisodeRepo
from src.infra.models import episode_schema

from src.api.interactor import ApiInteractor
from src.domain.episode import Episode, PostEpisodeInput

episode_repo = EpisodeRepo(engine, episode_schema)  # TODO: move this to fixture

MOCK_EPISODE: Episode = dict(
    id="9b81efb6-e8a1-11ec-9e1d-eb36b3ac7ec2",
    episodeTitle="Economics 101",
    podcastTitle="Money and Fame",
    thumbnailUrl="https://example.com/somethumbnail.png",
    guests=[dict(name="Adam Smith"), dict(name="Karl Marx")],
    audioUrl="https://example.com/episode_economics_101.mp3",
    episodeDurationSeconds=2100,
)


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
def mock_read_episodes_response(monkeypatch):
    """Provide the mock response of read_episodes methods (of EpisodeRepo class)"""

    def mock_read_episodes():
        return [Episode(**MOCK_EPISODE)]

    monkeypatch.setattr(episode_repo, "read_episodes", mock_read_episodes)


@pytest.fixture
def mock_create_episode_response(monkeypatch):
    """Provide the mock response of create_episode methods (of EpisodeRepo class)"""

    def mock_create_episode(payload: PostEpisodeInput):
        new_id = uuid4()
        return Episode(**payload, id=new_id)

    monkeypatch.setattr(episode_repo, "create_episode", mock_create_episode)


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
def api_interactor(
    mock_read_episode_response,
    mock_read_episodes_response,
    mock_create_episode_response,
    mock_delete_episode_response,
):
    return ApiInteractor(episode_repo)
