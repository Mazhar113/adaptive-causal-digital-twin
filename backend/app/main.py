
from fastapi import FastAPI
from .db import init_db
init_db()
app = FastAPI(title="Adaptive & Causal Digital Twin - Slim")
@app.get("/health")
def health():
    return {"status":"ok"}
