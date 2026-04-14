from fastapi import FastAPI

app = FastAPI(title="Veilborn API", version="0.1.0")

@app.get("/")
def root():
    return {"message": "Welcome to the Veilborn API"}
