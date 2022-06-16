""" 
This module contains the Pydantic models that define the core data structure (input, output, core models).
"""
from uuid import UUID
from typing import List, Dict, Union
from pydantic import BaseModel


class Person(BaseModel):
    name: str


class PostEpisodeInput(BaseModel):
    episodeTitle: str
    postcaseTitle: str
    thumbnailUrl: str
    guests: List[Person]
    audioUrl: str
    episodeDurationSeconds: int


class PostEpisodeOutput(BaseModel):
    resourceUrl: Union[str, None]


class Episode(BaseModel):
    id: UUID
    episodeTitle: str
    podcastTitle: str
    thumbnailUrl: str
    guests: List[Person]
    audioUrl: str
    episodeDurationSeconds: int
