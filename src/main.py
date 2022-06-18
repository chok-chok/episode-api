from fastapi import FastAPI, HTTPException

from typing import Union
from domain.episode import Episode, PostEpisodeInput, PostEpisodeOutput

from .dependency import interactor

app = FastAPI()


@app.get("/")
def read_root():
    return {"data": "the start of a long journey"}


@app.get("/episodes/{episode_id}", status_code=200, response_model=Episode)
def get_episode(episode_id: str):
    result = interactor.execute_get_episode(episode_id)

    if result is None:
        raise HTTPException(status_code=404, detail="Episode not found")


@app.post("/episodes/", status_code=201, response_model=PostEpisodeOutput)
def post_episode(payload: PostEpisodeInput):
    payload = dict(payload)
    return interactor.execute_post_episode(payload)


"""
@app.get("/episodes")
def read_episodes():
    data = api.read_episodes()
    return {"data": data}

@app.delete("/episodes/{episode_id}")
def delete_episode(episode_id: int):
    return {"data": "return result here"}
"""
