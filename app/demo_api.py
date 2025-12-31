"""from fastapi import APIRouter, HTTPException, Body
from app.translator import translate_text
from fastapi.responses import PlainTextResponse


router = APIRouter(prefix="/demo", tags=["Demo"])

@router.post("/translate", response_class=PlainTextResponse)
def demo_translate(
    body: str = Body(..., media_type="text/plain")
):
    if "English:" not in body or "Domain:" not in body:
        return PlainTextResponse(
            "Invalid format.\n\n"
            "Please use:\n"
            "Domain: healthcare\n"
            "English: How are you feeling today?\n",
            status_code=400
        )

    return (
        "✅ Demo received!\n\n"
        "This endpoint shows how translation works.\n"
        "For real translations, use /translate.\n"
    )
@router.get("/demo", response_class=PlainTextResponse)
def demo():
    return (
        "👋 Welcome to the Translation Demo\n\n"
        "Try copying a sentence and translating it.\n\n"
        "This system prioritizes:\n"
        "- Human-verified translations\n"
        "- Healthcare-safe language\n"
        "- Standard Haitian Creole\n\n"
        "Use /translate or /translate/long to begin."
    )"""