from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from views.users import router as users_router

app = FastAPI()

origins = [
    'http://localhost',
    'http://localhost:8080',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(users_router, prefix='/users')
