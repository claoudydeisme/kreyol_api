from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader
import os

API_KEY_HEADER = APIKeyHeader(name="X-API-Key", auto_error=False)

# Example in-memory store (replace with DB later)
REVIEWER_KEYS = {
    key.strip(): "REVIEWER"
    for key in os.getenv("REVIEWER_API_KEYS", "").split(",")
    if key.strip()
}
print("Loaded reviewer keys:", list(REVIEWER_KEYS.keys()))

def get_current_role(api_key: str = Security(API_KEY_HEADER)) -> str:
    if not api_key: #or api_key not in REVIEWER_KEYS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API key missing"
        )
    if api_key not in REVIEWER_KEYS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key"
        )

    return REVIEWER_KEYS[api_key]


def require_reviewer(role: str = Security(get_current_role)) -> str:
   
    #role is guaranteed for now
    return role

""" if role not in ("REVIEWER", "ADMIN"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Reviewer access required"
        )
"""
