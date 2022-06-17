"""ApiInteractor is a class with CRUD logics for REST endpoints. It takes DB-access module as dependency in runtime"""

from uuid import UUID
from typing import List, Union

from pydantic import ValidationError

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
        except Exception as e:
            ## TODO: properly handle unexpected exceptions
            print(f"Unexpected exceptions: {str(e)}")

    def exescute_get_episodes(self) -> List[Episode]:
        # TODO: apply pagination
        # Retrieve list of episodes with default pagination
        # If there is argument coming in for pagination use take to chop the list
        # TODO: (Optionally) consider to apply default sorting
        try:
            return self.db_access.read_episodes()
        except Exception as e:
            ## TODO: properly handle unexpected exceptions
            print(f"Unexpected exceptions: {str(e)}")

    def execute_post_episode(self, input: PostEpisodeInput) -> PostEpisodeOutput:
        try:
            PostEpisodeInput(**input)  # validate the input
            new_episode = self.db_access.create_episode(input)
            output = dict(resourceUrl=f"/episodes/{new_episode.id}")
            return PostEpisodeOutput(**output)
        except ValidationError as e:
            raise e
        except Exception as e:
            ## TODO: properly handle unexpected exceptions
            print(f"Unexpected exceptions: {str(e)}")

    def execute_del_episode(self, id: UUID) -> Union["Success", "Fail"]:
        try:
            parsed_id = _parse_id(id)
            return self.db_access.delete_episode(
                parsed_id
            )  ##TODO: Handle episode lookup in db-access
        except ValueError:
            raise ValueError("Invalid uuid format")
        except Exception as e:
            ## TODO: properly handle unexpected exceptions
            print(f"Unexpected exceptions: {str(e)}")
