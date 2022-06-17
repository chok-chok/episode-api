"""ApiInteractor is a class with CRUD logics for REST endpoints. It takes DB-access module as dependency in runtime"""

from uuid import UUID
from typing import List, Union

from domain.episode import Episode, PostEpisodeInput, PostEpisodeOutput
from infra.storage import EpisodeRepo


def _parse_id(value):
    try:
        result = UUID(value)
        return result
    except ValueError:
        raise ValueError


class ApiInteractor:
    def __init__(self, db_access: EpisodeRepo):
        self.db_access = db_access

    def execute_get_episode(self, id: str) -> Union[Episode, None]:
        try:
            parsed_id = _parse_id(id)
            return self.db_access.read_episode(parsed_id)
        except ValueError:
            raise ValueError("Invalid uuid format")
        except Exception:
            raise Exception("Unexpected exception")

    def execute_get_episodes(self) -> List[Episode]:
        """Read list of episode from database"""
        # Retrieve list of episodes with default pagination
        # If there is argument coming in for pagination use take to chop the list
        # (Optionally) consider to apply default sorting
        pass

    def execute_post_episode(self, input: PostEpisodeInput) -> PostEpisodeOutput:
        # Take payload to create a new episode
        # (Consider to validate the payload)
        # Raise exception when the payload is invalid
        # Pass the payload to db-access
        # Return the URL to new data
        pass

    def execute_del_episode(self, id: UUID) -> Union["Success", "Fail"]:
        # Take id to delete the episode
        # Check if episode exists
        # Return None if it doesn't
        # Pass the ID to DB-access
        # Return success message to caller
        pass
