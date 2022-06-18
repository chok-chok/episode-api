from infra.storage import EpisodeRepo
from infra.models import episode_schema
from infra.db import engine

from api.interactor import ApiInteractor

repo = EpisodeRepo(engine, episode_schema)

interactor = ApiInteractor(repo)
