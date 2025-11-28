from fastapi import FastAPI
from app.auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Authentication API")

origins = [
    "http://localhost:3000",
    "https://jobscout-frontend-production.up.railway.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origins=["*"],
)

app.include_router(auth_router)

@app.get("/")
def read_root():
    return {"msg": "Auth API running"}
