from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import db_path

# engine is only needed during database init and session init
engine = create_engine(
    db_path, pool_pre_ping=True, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
