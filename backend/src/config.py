import os
from dotenv import load_dotenv
load_dotenv()

SQL_HOST = os.getenv("SQL_HOST")
SQL_USER = os.getenv("SQL_USER")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")
SQL_DB = os.getenv("SQL_DB")
SQL_URL = f"postgresql://{SQL_USER}:{SQL_PASSWORD}@{SQL_HOST}/{SQL_DB}"

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
TIMEZONE = os.getenv("TIMEZONE")
PORT = int(os.getenv("PORT"))
API_KEY = os.getenv("API_KEY")