""" 
This module contains the Pydantic models that define the core data structure (input, output, core models).
"""
from uuid import UUID
from typing import List
from pydantic import BaseModel


class Person(BaseModel):
    name: str


class PostEpisodeInput(BaseModel):
    episodeTitle: str
    podcastTitle: str
    thumbnailUrl: str
    guests: List[Person]
    audioUrl: str
    episodeDurationSeconds: int


class PostEpisodeOutput(BaseModel):
    resourceUrl: str


class DeleteEpisodeOutput(BaseModel):
    result: str  # TODO: use Literal type: either Success or Fail (require python >= 3.8)


class Episode(BaseModel):
    id: UUID  # uuid version 4
    episodeTitle: str
    podcastTitle: str
    thumbnailUrl: str
    guests: List[Person]
    audioUrl: str
    episodeDurationSeconds: int
