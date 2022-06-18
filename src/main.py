import logging
from fastapi import FastAPI, HTTPException

from typing import Union
from domain.episode import Episode

from .dependency import interactor

app = FastAPI()


@app.get("/")
def read_root():
    return {"data": "the start of a long journey"}


@app.get("/episodes/{episode_id}", status_code=200, response_model=Episode)
def get_episode(episode_id: str):
    try:
        result = interactor.execute_get_episode(episode_id)

        if result is None:
            raise HTTPException(status_code=404, detail="Episode not found")
        else:
            return {"data": result}
    except ValueError as e:
        # TODO: properly format the logging
        logging.exception(f"Exception occur: {e}")
        raise HTTPException(status_code=422, detail=str(e))


"""
@app.get("/episodes")
def read_episodes():
    data = api.read_episodes()
    return {"data": data}


@app.post("/episodes")
def create_episode():
    return {"data": "return a full episode here"}


@app.delete("/episodes/{episode_id}")
def delete_episode(episode_id: int):
    return {"data": "return result here"}
"""
