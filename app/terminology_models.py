from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TermEntry(BaseModel):
    id: str
    domain: str
    source_language: str
    target_language: str
    source_term: str
    target_term: str
    approved: bool = False
    created_by: str
    reviewed_by: Optional[str] = None
    created_at: datetime
    reviewed_at: Optional[datetime] = None
