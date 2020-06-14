from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.views.users import router as users_router
from app.views.table import router as table_router

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(users_router, prefix='/users')
app.include_router(table_router, prefix='/table')
