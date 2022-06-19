"""Schema definition for postgres"""

from sqlalchemy import MetaData, Table, Column, String, Integer, JSON
from sqlalchemy.dialects.postgresql import UUID

import uuid

from .db import engine

metadata_obj = MetaData()

episode_schema = Table(
    "episode",
    metadata_obj,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4()),
    Column("episodeTitle", String(100), nullable=False),
    Column("podcastTitle", String(100), nullable=False),
    Column("thumbnailUrl", String(100), nullable=False),
    Column("guests", JSON, default=[]),
    Column("audioUrl", String(100), nullable=False),
    Column("episodeDurationSeconds", Integer, nullable=False),
)

# Create a new table if doens't exist
episode_schema.create(engine, checkfirst=True)
