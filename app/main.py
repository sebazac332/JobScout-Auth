from fastapi import FastAPI
from app.auth import router as auth_router

app = FastAPI(title="Authentication API")

app.include_router(auth_router)

@app.get("/")
def read_root():
    return {"msg": "Auth API running"}
