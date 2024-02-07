from databases import Database
from sqlalchemy import create_engine
from src.config import SQL_URL

db = Database(SQL_URL)