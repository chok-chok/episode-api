from fastapi import FastAPI
from typing import Union
from helloworld import msg

app = FastAPI()

@app.get("/")
def read_root():
    return {"data": "the start of a long journey"}


@app.get("/episodes/{episode_id}")
def read_episode(episode_id: int, q: Union[str, None] = None):
    return {"episode_id": episode_id, "q": q}

@app.get("/episodes")
def read_episodes():
    return {"data": "return list of episodes"}

@app.post("/episodes")
def create_episode():
    return {"data": "return a full episode here"}

@app.delete("/episodes/{episode_id}")
def delete_episode(episode_id: int):
    return {"data": "return result here"}