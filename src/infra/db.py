from sqlalchemy import create_engine
from config import config

db_user, db_pwd = config["POSTGRES_USERNAME"], config["POSTGRES_PASSWORD"]

engine = create_engine(f"postgresql://{db_user}:{db_pwd}@localhost:5432/episodedb")
