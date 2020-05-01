import os

SQLITE = True

if SQLITE:
    BASE_DIR = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '..', 'database'
    )
    db_path = BASE_DIR.replace("\\", "/") + '/db.sqlite'
    sqlite_db_path = 'sqlite:///' + db_path
else:
    pass
