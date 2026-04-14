from fastapi import FastAPI
from .database import engine, Base
from . import models
from .routers import heroes

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Veilborn API", version="0.1.0")

app.include_router(heroes.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Veilborn API"}
