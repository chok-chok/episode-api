# Local setup
To set up the development environment on a local machine, follow the steps described below.

## System requirements
- OS: tested on `Ubuntu` and `MacOS`, but recommend `Ubuntu 20.04.4 LTS`
- Database: tested on `Postgres 12`

---
## 1. Install Poetry (package manager)
- Follow [the installation guide](https://python-poetry.org/docs/#installation)

## 2. Install dependencies and setup venv 
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
- Copy the venv path from the above output (e.g. `~/.cache/pypoetry/virtualenvs/python-api-example-R7RR5aY2-py3.8`) 
- Paste it to the Python interpreter path at your IDE
- (Optionally) restart the terminal in your IDE
- Finally install dependencies by running `poetry install`

## 3. Launch the app 
All set! just run the following command from the root folder of the project.
```
  uvicorn src.main:app --reload
```
And..
```
  Call the API running locally on: http://127.0.0.1:8000
```
---

# Before committing a new change:
Please follow these two steps before commiting any new changes.

## 1. Format the code
- This project uses [Black](https://black.readthedocs.io) for code formatting. 
- Before committing any change, run ` black ./`

## 2. Run tests
- This project uses [pytest](https://docs.pytest.org/en/7.1.x/) for unit tests & integration test. 
- Run `pytest` (this will run all tests in the project)
  - Tests for the DB-access module depend on the testdb setup
  - Therefore, please ensure `Postgres` is installed & running locally before running tests


