import pytest

from pydantic import ValidationError
from .conftest import MOCK_EPISODE
from ..helpers import validate_uuid

from src.api.interactor import ApiInteractor
from src.domain.episode import (
    Episode,
    PostEpisodeInput,
    PostEpisodeOutput,
    DeleteEpisodeOutput,
)

NULL_CASE_ID = "9b81efb6-e8a1-11ec-9e1d-eb36b3ac7eF5"
INVALID_ID = "e8a1_9b81efb6_11ec_9e13"

CREATE_EPISODE_INPUT: PostEpisodeInput = dict(
    episodeTitle="Debt based monetary system",
    podcastTitle="Money and Fame",
    thumbnailUrl="https://example.com/somethumbnail_2.png",
    guests=[dict(name="John Maynard Keynes")],
    audioUrl="https://example.com/episode_currency_and_money.mp3",
    episodeDurationSeconds=3000,
)

# CREATE_EPISODE_INVALID_INPUT: missing podcastTitle field
CREATE_EPISODE_INVALID_INPUT = dict(
    episodeTitle="Debt based monetary system",
    thumbnailUrl="https://example.com/somethumbnail_2.png",
    guests=[dict(name="John Maynard Keynes")],
    audioUrl="https://example.com/episode_currency_and_money.mp3",
    episodeDurationSeconds=3000,
)

# Tests for execute_get_episode method
def test_get_episode_success_case(api_interactor: ApiInteractor):
    """Should return correct episode (instance of Episode)"""
    output = api_interactor.execute_get_episode(MOCK_EPISODE["id"])
    assert output == Episode(**MOCK_EPISODE)


def test_get_episode_null_case(api_interactor: ApiInteractor):
    """Should return None when episode is not found"""
    output = api_interactor.execute_get_episode(NULL_CASE_ID)
    assert output == None


def test_get_episode_invalid_id(api_interactor: ApiInteractor):
    """Should raise ValueError when the format of id is invalid"""
    with pytest.raises(ValueError) as err_info:
        api_interactor.execute_get_episode(INVALID_ID)
    assert "Invalid uuid format" in str(err_info.value)


# Tests for execute_get_episode method
# TODO: Add more test cases: e.g with pagination
def test_get_episodes_success(api_interactor: ApiInteractor):
    """Should return list of episode with correct length"""
    output = api_interactor.exescute_get_episodes(limit=20, offset=0)
    assert len(output) == 1


# Tests for execute_post_episode method
def test_post_episode_success_case(api_interactor: ApiInteractor):
    """Should return resource url as output"""
    output = api_interactor.execute_post_episode(CREATE_EPISODE_INPUT)
    splitted_output = output.resourceUrl.split("/")
    resource_path, resource_id = splitted_output[1], splitted_output[2]
    assert resource_path == "episodes"
    assert validate_uuid(resource_id) == True


def test_post_episode_invalid_input(api_interactor: ApiInteractor):
    """Should raise ValidationError when the input is invalid"""
    with pytest.raises(ValidationError):
        api_interactor.execute_post_episode(CREATE_EPISODE_INVALID_INPUT)


# Tests for execute_del_episode method
def test_del_episode_success_case(api_interactor: ApiInteractor):
    """Should return correct output with Success as result"""
    output = api_interactor.execute_del_episode(MOCK_EPISODE["id"])
    assert output.result == "Success"


def test_del_episode_null_case(api_interactor: ApiInteractor):
    """Should return correct output with Fail as result"""
    output = api_interactor.execute_del_episode(NULL_CASE_ID)
    assert output.result == "Fail"


def test_del_episode_invalid_id(api_interactor: ApiInteractor):
    """Should raise ValueError when the format of id is invalid"""
    with pytest.raises(ValueError) as err_info:
        api_interactor.execute_del_episode(INVALID_ID)
    assert "Invalid uuid format" in str(err_info.value)
