Python api example project

## Steps to run the project locally

#### 1. Prerequisites 
- Ensure [the poetry is installed](https://python-poetry.org/docs/#installation)
- Install dependencies by running `poetry install`
- Check venv path of poetry by running `poetry env info` 
```
Virtualenv
Python:         3.8.10
Implementation: CPython
Path:           /home/koelkast/.cache/pypoetry/virtualenvs/python-api-example-R7RR5aY2-py3.8
Valid:          True

System
Platform: linux
OS:       posix
Python:   /usr
```
- Add the virtualenv path to your IDE's Python intepreter path 

#### 2. Launch the app (from root folder of project)
```
  uvicorn src.main:app --reload
```
```
  Call the API running locally on: http://127.0.0.1:8000
```

## Code formatting
This project uses [Black](https://black.readthedocs.io) for code formatting. 

Before commiting the code, run the following command:

```
  black ./src
```

