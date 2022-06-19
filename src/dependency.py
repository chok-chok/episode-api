from infra.storage import EpisodeRepo
from infra.models import episode_schema
from infra.db import engine

from app.interactor import Interactor

repo = EpisodeRepo(engine, episode_schema)

interactor = Interactor(repo)
