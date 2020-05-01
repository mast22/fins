from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_config import sqlite_db_path

# engine is only needed during database init and session init
engine = create_engine(sqlite_db_path, pool_pre_ping=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
