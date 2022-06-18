"""EpisodeRepo is responsible for database access. It provides interfaces to perform DB operations"""

from uuid import UUID
from typing import List
from sqlalchemy import sql
from domain.episode import Episode, PostEpisodeInput
from infra.models import episode_schema


class EpisodeRepo:
    def __init__(self, db_engine, schema: episode_schema):
        self.db = db_engine
        self.episode = schema

    def read_episode(self, id: UUID) -> Episode:
        """
        Retrieve the record using the given UUID.
        Return Episode object
        """
        try:
            select = self.episode.select().where(self.episode.c.id == id)

            result = self.db.execute(select).fetchone()

            if result is None:
                return None
            else:
                return Episode(**result)
        except Exception as e:
            print(f"Unexpected exceptions: {str(e)}")
            raise e

    def read_episodes(self) -> List[Episode]:
        """
        Retrieve the records
        Return list of Episode objects

        TO support pagination as next step
        """
        pass

    def create_episode(self, input: PostEpisodeInput) -> Episode:
        """
        Write a new report using the input
        New UUID4 is created

        Return Episode object
        """
        pass

    def delete_episode(self, id: UUID) -> str:
        """
        Check if the episode exist, return None if not

        Delete the episode and return the result
        """
        pass
