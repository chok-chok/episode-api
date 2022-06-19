from sqlalchemy import create_engine

from config import DB_HOST, DB_USER, DB_PWD

print(DB_USER)
engine = create_engine(f"postgresql://{DB_USER}:{DB_PWD}@{DB_HOST}:5432/episodedb")
