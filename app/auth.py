from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from app.utils import verify_password, create_access_token, SECRET_KEY, ALGORITHM
from app.db import get_db
from app.models import User, Admin

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    admin = db.query(Admin).filter(Admin.email == form_data.username).first()
    account = user or admin

    if not account or not verify_password(form_data.password, account.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    role = "admin" if admin else "user"
    access_token = create_access_token({"sub": account.email, "role": role})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/verify")
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {"email": payload.get("sub"), "role": payload.get("role")}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")