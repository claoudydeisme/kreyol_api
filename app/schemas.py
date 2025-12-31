from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class TranslationOptions(BaseModel):
    preserve_paragraphs: bool = True
    speech_safe: bool = True


class TranslationRequest(BaseModel):
    text: str = Field(..., min_length=1)
    source_language: Optional[str] = None
    target_language: Optional[str] = None
    domain: str
    options: Optional[TranslationOptions] = TranslationOptions()


class TranslationResponse(BaseModel):
    translation: str
    source_language: str
    target_language: str
    domain: str
    confidence: float
    warnings: List[str] = []

class LongTranslationRequest(BaseModel):
    text: str
    source_language: Optional[str] = None
    target_language: Optional[str] = None
    domain: str
    #options: Optional[TranslationOptions] = TranslationOptions()

class LongTranslationResponse(BaseModel):
    sections: list
    source_language: str
    target_language: str
    domain: str
    average_confidence: float
    warnings: list[str]

class TerminologyProposeRequest(BaseModel):
    domain: str
    source_language: str
    target_language: str
    source_term: str
    target_term: str
    created_by: str


"""class TerminologyApproveRequest(BaseModel):
    term_id: str
    reviewed_by: str
"""

class TerminologyResponse(BaseModel):
    id: str
    domain: str
    source_language: str
    target_language: str
    source_term: str
    target_term: str
    approved: bool
    created_by: str
    reviewed_by: Optional[str]
    created_at: datetime
    reviewed_at: Optional[datetime]


class ApproveTermRequest(BaseModel):
    term_id: str
