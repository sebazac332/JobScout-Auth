from fastapi import FastAPI
from app.auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Authentication API")

app.add_middleware(
    CORSMiddleware,
    allow_origins="https://jobscout-frontend-production.up.railway.app",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)

@app.get("/")
def read_root():
    return {"msg": "Auth API running"}
