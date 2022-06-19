from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = "localhost" if os.environ.get("RUN_LOCAL") else "postgres"
DB_USER = os.environ.get("POSTGRES_USERNAME")
DB_PWD = os.environ.get("POSTGRES_PASSWORD")

BASIC_AUTH_USER = os.environ.get("BASIC_AUTH_USERNAME")
BASIC_AUTH_PWD = os.environ.get("BASIC_AUTH_PASSWORD")
