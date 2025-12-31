from fastapi import APIRouter, HTTPException, Depends
from app.schemas import (
    TerminologyProposeRequest,
    #TerminologyApproveRequest,
    TerminologyResponse,
    ApproveTermRequest
)
from app.terminology_registry import TerminologyRegistry
from app.config import SUPPORTED_DOMAINS
from app.security import require_reviewer
import logging


router = APIRouter()

router = APIRouter(prefix="/terminology", tags=["Terminology"])
logger = logging.getLogger(__name__)
registry = TerminologyRegistry()


@router.post("/propose", response_model=TerminologyResponse)
def propose_term(req: TerminologyProposeRequest):
    if req.domain not in SUPPORTED_DOMAINS:
        raise HTTPException(status_code=400, detail="INVALID_DOMAIN")

    try:
        entry = registry.propose_term(req)
    except ValueError as e:
        raise HTTPException(
            status_code=409,
            detail=str(e)
        )

    return entry


""" 
    @router.post("/approve", response_model=TerminologyResponse)
    def approve_term(req: TerminologyApproveRequest):
    entry = registry.approve_term(req.term_id, req.reviewed_by)
    if not entry:
        raise HTTPException(status_code=404, detail="TERM_NOT_FOUND")
    return entry
    
"""


@router.get("/{domain}", response_model=list[TerminologyResponse])
def list_approved_terms(domain: str):
    if domain not in SUPPORTED_DOMAINS:
        raise HTTPException(status_code=400, detail="INVALID_DOMAIN")

    return registry.get_approved_terms_entries(domain)


#Approve endpoint
@router.post("/approve", response_model=TerminologyResponse)
def approve_term(
    req: ApproveTermRequest,
    #term_id: str,
    reviewer: str = Depends(require_reviewer)
):
   
    logger.info(
        "TERM_APPROVED",
        extra={
            "term_id": req.term_id,
            "reviewer": reviewer
        }
    )

    entry = registry.approve_term(req.term_id, reviewer)
    if not entry:
        raise HTTPException(status_code=404, detail="TERM_NOT_FOUND")
    

    return entry

@router.get("/auth/validate")
def validate_reviewer_key(
    role: str = Depends(require_reviewer)
):
    return {
        "status": "valid",
        "role": role
    }
