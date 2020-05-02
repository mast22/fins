import os

SQLITE = True

if SQLITE:
    BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'db')
    location = BASE_DIR.replace("\\", "/") + '/db.sqlite'
    db_path = 'sqlite:///' + location
else:
    db_path = 'postgresql://root:root@localhost:5432/db'
