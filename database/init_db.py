import os
from sqlalchemy import create_engine
from models import Base

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

db_path = BASE_DIR.replace("\\", "/") + '/db.sqlite'

try:
    # удаляем если существует
    os.remove(db_path)
except:
    pass

sqlite_db_path = 'sqlite:///' + db_path

engine = create_engine(sqlite_db_path, echo=True)

Base.metadata.create_all(engine)
