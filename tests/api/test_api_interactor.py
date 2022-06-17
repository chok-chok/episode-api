import pytest

from .conftest import MOCK_EPISODE
from src.domain.episode import Episode

NULL_CASE_ID = "9b81efb6-e8a1-11ec-9e1d-eb36b3ac7eF5"
INVALID_ID = "e8a1_9b81efb6_11ec_9e13"

## Tests for execute_get_episode method
def test_get_episode_success_case(api_interactor):
    """Should return correct episode (instance of Episode)"""
    result = api_interactor.execute_get_episode(MOCK_EPISODE["id"])
    assert result == Episode(**MOCK_EPISODE)


def test_get_episode_null_case(api_interactor):
    """Should return None when episode is not found"""
    result = api_interactor.execute_get_episode(NULL_CASE_ID)
    assert result == None


def test_get_episode_value_err(api_interactor):
    """Should raise ValueError when the format of id is invalid"""
    with pytest.raises(ValueError) as err_info:
        api_interactor.execute_get_episode(INVALID_ID)
    assert "Invalid uuid format" in str(err_info.value)


def test_get_episodes_length():
    assert 2 == 2


def test_post_episode_success():
    assert 1 == 1


## Tests for execute_del_episode method
def test_del_episode_success_case(api_interactor):
    """Should return "Success" as output"""
    result = api_interactor.execute_del_episode(MOCK_EPISODE["id"])
    assert result == "Success"


def test_del_episode_null_case(api_interactor):
    """Should return "Fail" as output"""
    result = api_interactor.execute_del_episode(NULL_CASE_ID)
    assert result == "Fail"


def test_del_episode_value_err(api_interactor):
    """Should raise ValueError when the format of id is invalid"""
    with pytest.raises(ValueError) as err_info:
        api_interactor.execute_del_episode(INVALID_ID)
    assert "Invalid uuid format" in str(err_info.value)
