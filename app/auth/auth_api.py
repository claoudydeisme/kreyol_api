"""from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.auth.oauth import create_access_token, USERS

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/token")
def login(form: OAuth2PasswordRequestForm = Depends()):
    user = USERS.get(form.username)
    if not user:
        return {"error": "invalid credentials"}

    token = create_access_token(
        {"sub": user["username"], "role": user["role"]}
    )
    return {
        "access_token": token,
        "token_type": "bearer"
    }
"""