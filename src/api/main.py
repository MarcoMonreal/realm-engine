from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from . import models
from .routers import heroes, combat

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Veilborn API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:5173"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.include_router(heroes.router)
app.include_router(combat.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Veilborn API"}
