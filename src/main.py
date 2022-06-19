import secrets
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from typing import Union, List
from domain.episode import (
    Episode,
    PostEpisodeInput,
    PostEpisodeOutput,
    DeleteEpisodeOutput,
)

from .dependency import interactor
from config import config


security = HTTPBasic()


def basic_auth(cred: HTTPBasicCredentials = Depends(security)):
    correct_user = secrets.compare_digest(cred.username, config["BASIC_AUTH_USERNAME"])
    correct_pwd = secrets.compare_digest(cred.password, config["BASIC_AUTH_PASSWORD"])

    if not (correct_user and correct_pwd):
        raise HTTPException(
            status_code=401,
            detail="Unauthroized request",
            headers={"WWW-Authenticate": "Basic"},
        )
    return cred.username


app = FastAPI(dependencies=[Depends(basic_auth)])


@app.get("/")
def read_root():
    return "root"


@app.get("/episodes", status_code=200, response_model=List[Episode])
def get_episodes():
    return interactor.exescute_get_episodes()


@app.get("/episodes/{episode_id}", status_code=200, response_model=Episode)
def get_episode(episode_id: str):
    result = interactor.execute_get_episode(episode_id)

    if result is None:
        raise HTTPException(status_code=404, detail="Episode not found")
    return result


@app.post("/episodes", status_code=201, response_model=PostEpisodeOutput)
def post_episode(payload: PostEpisodeInput):
    payload = dict(payload)
    return interactor.execute_post_episode(payload)


@app.delete(
    "/episodes/{episode_id}", status_code=200, response_model=DeleteEpisodeOutput
)
def delete_episode(episode_id: str):
    return interactor.execute_del_episode(episode_id)
