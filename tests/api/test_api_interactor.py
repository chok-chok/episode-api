from pydantic import ValidationError
import pytest

from .conftest import MOCK_EPISODE
from ..helpers import validate_uuid

from src.domain.episode import Episode, PostEpisodeInput, PostEpisodeOutput

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
def test_get_episode_success_case(api_interactor):
    """Should return correct episode (instance of Episode)"""
    result = api_interactor.execute_get_episode(MOCK_EPISODE["id"])
    assert result == Episode(**MOCK_EPISODE)


def test_get_episode_null_case(api_interactor):
    """Should return None when episode is not found"""
    result = api_interactor.execute_get_episode(NULL_CASE_ID)
    assert result == None


def test_get_episode_invalid_id(api_interactor):
    """Should raise ValueError when the format of id is invalid"""
    with pytest.raises(ValueError) as err_info:
        api_interactor.execute_get_episode(INVALID_ID)
    assert "Invalid uuid format" in str(err_info.value)


def test_get_episodes_length():
    assert 2 == 2


# Tests for execute_post_episode method
def test_post_episode_success_case(api_interactor):
    """Should return resource url as output"""
    result: PostEpisodeOutput = api_interactor.execute_post_episode(
        CREATE_EPISODE_INPUT
    )
    splitted_output = result.resourceUrl.split("/")
    resource_path, resource_id = splitted_output[1], splitted_output[2]
    assert resource_path == "episodes"
    assert validate_uuid(resource_id) == True


def test_post_episode_invalid_input(api_interactor):
    """Should raise ValidationError when the input is invalid"""
    with pytest.raises(ValidationError):
        api_interactor.execute_post_episode(CREATE_EPISODE_INVALID_INPUT)


# Tests for execute_del_episode method
def test_del_episode_success_case(api_interactor):
    """Should return "Success" as output"""
    result = api_interactor.execute_del_episode(MOCK_EPISODE["id"])
    assert result == "Success"


def test_del_episode_null_case(api_interactor):
    """Should return "Fail" as output"""
    result = api_interactor.execute_del_episode(NULL_CASE_ID)
    assert result == "Fail"


def test_del_episode_invalid_id(api_interactor):
    """Should raise ValueError when the format of id is invalid"""
    with pytest.raises(ValueError) as err_info:
        api_interactor.execute_del_episode(INVALID_ID)
    assert "Invalid uuid format" in str(err_info.value)
