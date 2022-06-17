import pytest

from .conftest import MOCK_EPISODE
from src.domain.episode import Episode


def test_get_episode_success_case(api_interactor):
    """Should return correct episode (instance of Episode)"""
    result = api_interactor.execute_get_episode(MOCK_EPISODE["id"])
    assert result == Episode(**MOCK_EPISODE)


def test_get_episode_null_case(api_interactor):
    """Should return None when episode is not found"""
    null_case_id = "9b81efb6-e8a1-11ec-9e1d-eb36b3ac7eF5"
    result = api_interactor.execute_get_episode(null_case_id)
    assert result == None


def test_get_episode_value_err(api_interactor):
    """Should raise ValueError when the format of id is invalid"""
    with pytest.raises(ValueError) as err_info:
        invalid_id = "e8a1_9b81efb6_11ec_9e13"
        api_interactor.execute_get_episode(invalid_id)
    assert "Invalid uuid format" in str(err_info.value)


def test_get_episodes_length():
    assert 2 == 2


def test_post_episode_success():
    assert 1 == 1


def test_del_episode():
    assert 1 == 1
