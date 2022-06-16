"""ApiInteractor is a class with CRUD logics for REST endpoints. It takes DB-access module as dependency in run-time"""

from uuid import UUID
from typing import List, Dict
from domain.episode import Episode, PostEpisodeInput, PostEpisodeOutput

from storage import EpisodeStorage


class ApiInteractor:
    def __init__(self, db_access: EpisodeStorage):
        self.db_access = db_access

    def execute_get_episode(id: UUID) -> Episode:
        # Take the id of episode
        # Check if the episode exists
        # Return None if it doesn't, otherwise return Episode
        pass

    def execute_get_episodes() -> List[Episode]:
        """Read list of episode from database"""
        # Retrieve list of episodes with default pagination
        # If there is argument coming in for pagination use take to chop the list
        # (Optionally) consider to apply default sorting
        pass

    def execute_post_episode(input: PostEpisodeInput) -> PostEpisodeOutput:
        # Take payload to create a new episode
        # (Consider to validate the payload)
        # Raise exception when the payload is invalid
        # Pass the payload to db-access
        # Return the URL to new data
        pass

    def execute_del_episode(id: UUID) -> Union["Success", "Fail"]:
        # Take id to delete the episode
        # Check if episode exists
        # Return None if it doesn't
        # Pass the ID to DB-access
        # Return success message to caller
        pass
