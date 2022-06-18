"""ApiInteractor is a class with CRUD logics for REST endpoints. It takes DB-access module as dependency in runtime"""

from uuid import UUID
from typing import List, Union

from pydantic import ValidationError

from domain.episode import (
    Episode,
    PostEpisodeInput,
    PostEpisodeOutput,
    DeleteEpisodeOutput,
)
from infra.storage import EpisodeRepo


class ApiInteractor:
    def __init__(self, db_access: EpisodeRepo):
        self.db_access = db_access

    def execute_get_episode(self, id: str) -> Union[Episode, None]:
        try:
            id = self._get_valid_uuid(id)
            return self.db_access.read_episode(id)
        except ValueError:
            raise ValueError("Invalid uuid format")
        except Exception as e:
            raise e

    def exescute_get_episodes(self) -> List[Episode]:
        # TODO: apply pagination
        # Retrieve list of episodes with default pagination
        # If there is argument coming in for pagination use take to chop the list
        try:
            return self.db_access.read_episodes()
        except Exception as e:
            ## TODO: properly handle unexpected exceptions
            print(f"Unexpected exceptions: {str(e)}")
            raise e

    def execute_post_episode(self, input: PostEpisodeInput) -> PostEpisodeOutput:
        try:
            # FastAPI layer validate the input at the REST endpoint
            # Making below line effectively duplicated validation

            # However, decided to keep this validation at interactor
            # To be prepared for different interface besides API framework
            # E.g. command line interface
            PostEpisodeInput(**input)
            new_episode = self.db_access.create_episode(input)
            output = dict(resourceUrl=f"/episodes/{new_episode.id}")
            return PostEpisodeOutput(**output)
        except ValidationError as e:
            raise e
        except Exception as e:
            ## TODO: properly handle unexpected exceptions
            print(f"Unexpected exceptions: {str(e)}")
            raise e

    def execute_del_episode(self, id: UUID) -> DeleteEpisodeOutput:
        try:
            id = self._get_valid_uuid(id)
            delete_result = self.db_access.delete_episode(id)
            output = dict(result=delete_result)
            return DeleteEpisodeOutput(**output)
        except ValueError:
            raise ValueError("Invalid uuid format")
        except Exception as e:
            ## TODO: properly handle unexpected exceptions
            print(f"Unexpected exceptions: {str(e)}")
            raise e

    def _get_valid_uuid(self, value):
        try:
            result = UUID(value)
            return result
        except ValueError:
            raise ValueError

