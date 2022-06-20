# episode-api
Example API implemented for a technical assignment. ([see requirements](./docs/REQUIREMENT.md))

---

## How to run the project
For development purpose, please follow the [local setup guide](./docs/LOCALSETUP.md) instead.

### 0. Install docker & docker-compose
- This project uses `docker` and `docker-compose`
- Thus [Installation of Docker Engine](https://docs.docker.com/engine/install/) is required


### 1. Add the .env file 
This project depends on few runtime variables. 

- Create `.env` file in the project root folder
- Refer to `.env_example` for required values & expected format

### 2. Build the docker images
- Simply run `docker-compose build` from the root folder

### 3. Run the containers
- `POSTGRES_USER`, `POSTGRES_PASSWORD` env var are required at container runtime
- Run the following command:
```
    # username and password in the command should match the ones in `.env` file

    POSTGRES_USER=your_pg_usr POSTGRES_PASSWORD=your_pg_pwd docker-compose up 
```

### 4. Play with the project

- Check the Swagger doc at `http://127.0.0.1:8000/docs`
- Call the API from your browser or via [Postman](https://www.postman.com/s)

---

## Implementation details
This project loosely follows the Clean Architecture. 

- Important classes of the project are `Interactor` and `EpisodeRepo`:
    - `Interactor`: 
        - Provide CRUD logic to the framework layer, which is currently FAST API
        - If additional interface needs to be added (e.g. CLI), it can just call the instance of ApiInteractor 
    - `EpisodeRepo`:
        - Database access layer, hide the DB-access related details and provide abstractions
        - Depends on SQLAlchemy, also injected at runtime (No ORM, using SqlAlchemy core)

- Core data structures (Pydantic models) are defined at `/src/domain/episode.py` 
    - Classes in the module are sporadically used for typing & parse the data to object

- Dependencies are injected at `/src/dependency.py`

## Test setup
- `test_interactor.py`: Unit tests for the interactor. DB-access layer is mocked.
- `test_storage.py`: Integration tests, it actually calls `Postgres` to test all DB-access methods. 


## Further improvement ideas
- Adding CI via Github Action
- Add test suits for the REST endpoints
- Proper logging
- Polish up the generated SwaggerDocs
- Add database init script (currently database init is implemented in the codebase - `/src/infra/db.py`)
- Add `alembic` to the project

