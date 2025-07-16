# app/main.py
from fastapi import FastAPI
from .routers import user
from . import models, database
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Allow requests from your frontend origin
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router, prefix="/auth", tags=["Auth"])
