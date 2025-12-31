from fastapi import APIRouter, Depends
from app.security import require_reviewer
from app.datasets.dataset_store import parallel_dataset

router = APIRouter(prefix="/datasets", tags=["Datasets"])

@router.get("/parallel")
def list_parallel_pairs(
    source_language: str | None = None,
    target_language: str | None = None,
    domain: str | None = None,
):
    return parallel_dataset.filter(
        source_language=source_language,
        target_language=target_language,
        domain=domain
    )


@router.get("/parallel/reviewer")
def list_parallel_pairs_reviewer(
    reviewer: str = Depends(require_reviewer)
):
    return parallel_dataset.get_all()
