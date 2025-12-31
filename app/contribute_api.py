"""from fastapi import APIRouter, HTTPException
from app.review_queue import flag_for_human_review
from fastapi.responses import PlainTextResponse


router = APIRouter(prefix="/contribute", tags=["Contribute"])

@router.post("/parallel", response_class=PlainTextResponse)
def contribute_parallel(body: str):
    try:
        sections = body.split("\n\n")

        domain = sections[0].split(":", 1)[1].strip().lower()
        source_lang = sections[1].split(":", 1)[1].strip().lower()
        target_lang = sections[2].split(":", 1)[1].strip().lower()

        source_text = sections[3].replace("SOURCE:", "").strip()
        target_text = sections[4].replace("TARGET:", "").strip()

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid contribution format. Please follow the template."
        )

    if not source_text or not target_text:
        raise HTTPException(400, "Source and target text are required.")

    # Queue for reviewer approval (NOT auto-added)
    flag_for_human_review(
        source_text=source_text,
        translated_text=target_text,
        issues=[],
        domain=domain
    )

    return (
        "Thank you!\n\n"
        "Your contribution has been received and queued for review.\n"
        "A reviewer will verify it before inclusion."
    )
@router.get("/contribute", response_class=PlainTextResponse)
def contribute():
    return (
        "🤝 Contribute a Translation Pair\n\n"
        "Please write your contribution in this format:\n\n"
        "Domain:\n"
        "healthcare\n\n"
        "English:\n"
        "How are you feeling today?\n\n"
        "Haitian Creole:\n"
        "Kijan ou santi ou jodi a?\n\n"
        "Thank you for helping Haitian communities."
    )"""