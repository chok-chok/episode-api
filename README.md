# episode-api
Example api implemented as a technical assignment. [(requirements)](./REQUIREMENT.md) 

---

## How to run the project
- Use `docker-compose` to run the project ([installation of Docker Engine](https://docs.docker.com/engine/install/) is required)
- For development purpose, please follow the [local setup guide](./SETUP.md)

#### 1. Add the .env file 
This project depends on following runtime variables. 

- Create `.env` file in the project root folder
- Refer to `.env_example` for required values & expected format

#### 2. Build the docker images
- Simply run `docker-compose build` from the root folder

#### 3. Run the containers
- `POSTGRES_USER`, `POSTGRES_PASSWORD` env var are required at container runtime
- Run `POSTGRES_USER=your_pg_usr POSTGRES_PASSWORD=your_pg_pwd docker-compose up`
    - Those username and password should match the ones at `.env` file

#### 4. Play with the project

- Checkout Swagger doc at `http://127.0.0.1:8000/docs`
- Call the api from your browser or via [Postman](https://www.postman.com/s)

---

## Implementation details
This project loosely follow the Clean Architecture. Reason for loosely following the pattern is to keep the balance between `modular & testable code` AND `flexibility & without too much over-engineering`.

- Important classes of the project are `ApiInteractor` and `EpisodeRepo`
    - `ApiInteractor`: 
        - Provide CRUD logic to framework layer, which is currently FAST API
        - If additional impl of framework layer need to be added, it can call the instance of ApiInteractor
    - `EpisodeRepo`:
        - Database access layer, hide the db-access related details and provide clean interface

- Core data structures (Pydantic models) are defined at `/domain/episode.py` 
    - Classes in the module are sporadically used for typing & parse the data to object

- Dependencies are injected at `dependency.py`

## Test setup
- `test_interactor.py`: Unit tests for the interactor. db-access layer is mocked.
- `test_storage.py`: Integration tests, it actually calls postgres to test all db-access methods. 

## Deployment consideration
- If possible, my preference would be to deploy the project as K8S services 
    - This is due to the limited working knowledge with other platforms

## Futher improvement ideas
- Adding CI via Github Action
- Add test suits for REST endpoint
- Polish up the generated SwaggerDocs
- Add database init script (currently database init is implemented in the codebase - `/src/infra.db.py`)
- Add `alembic` to the project

