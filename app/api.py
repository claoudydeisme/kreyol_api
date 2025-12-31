from fastapi import APIRouter, HTTPException
from app.schemas import TranslationRequest, TranslationResponse
from app.config import *
from app.language_detection import detect_language
from app.translator import translate_text
from app.safety_checks import enforce_creole_rules, simplify_if_low_confidence, should_simplify, simplify_creole, enforce_creole_grammar
from app.utils import normalize_text, word_count
from app.logging import log_translation
from app.long_translator import translate_long_document
from app.schemas import LongTranslationRequest, LongTranslationResponse
from app.review_queue import flag_for_human_review



router = APIRouter()



@router.post("/translate", response_model=TranslationResponse)
def translate(req: TranslationRequest):
    if req.domain not in SUPPORTED_DOMAINS:
        raise HTTPException(status_code=400, detail="INVALID_DOMAIN")

    text = normalize_text(req.text)

    if word_count(text) > MAX_WORDS:
        raise HTTPException(status_code=413, detail="TEXT_TOO_LONG")

    # Language detection
    if not req.source_language:
        detected_lang, confidence = detect_language(text)
        source_language = detected_lang
    else:
        source_language = req.source_language

    target_language = req.target_language
    if source_language == target_language:
        raise HTTPException(status_code=400, detail="SOURCE_EQUALS_TARGET")

    translation, confidence = translate_text(
        text,
        source_language,
        target_language,
        req.domain
    )

    warnings = []
    grammar_issues = enforce_creole_grammar(translation)

    for issue in grammar_issues:
        warnings.append(issue["code"])

    if should_simplify(grammar_issues) or confidence < CONFIDENCE_THRESHOLD:
        translation = simplify_creole()
        warnings.append("SIMPLIFIED_FOR_SAFETY")
    if any(i["severity"] in ["CRITICAL", "WARNING"] for i in grammar_issues):
        flag_for_human_review(
            source_text=text,
            translated_text=translation,
            issues=grammar_issues,
            domain=req.domain
        )



   

    if confidence < CONFIDENCE_THRESHOLD:
        translation = simplify_creole(translation)
        warnings.append("LOW_CONFIDENCE_SIMPLIFIED")

        #warnings.extend(enforce_creole_rules(translation))

        #if confidence < CONFIDENCE_THRESHOLD:
        #translation = simplify_if_low_confidence(translation)
        #warnings.append("LOW_CONFIDENCE_SIMPLIFIED")

    log_translation(text, translation, confidence, req.domain)

    return TranslationResponse(
        translation=translation,
        source_language=source_language,
        target_language=target_language,
        domain=req.domain,
        confidence=confidence,
        warnings=warnings
    )
    
# for transalations with a struture of words greater than 300
@router.post("/translate/long", response_model=LongTranslationResponse)
def translate_long(req: LongTranslationRequest):
    text = normalize_text(req.text)

    if word_count(text) <= MAX_WORDS:
        raise HTTPException(
            status_code=400,
            detail="Use /translate for short text"
        )

    if req.domain not in SUPPORTED_DOMAINS:
        raise HTTPException(status_code=400, detail="INVALID_DOMAIN")

    if not req.source_language:
        source_language, _ = detect_language(text)
    else:
        source_language = req.source_language

    sections, avg_conf, warnings = translate_long_document(
        text,
        source_language,
        req.target_language,
        req.domain
    )

    return LongTranslationResponse(
        sections=sections,
        source_language=source_language,
        target_language=req.target_language,
        domain=req.domain,
        average_confidence=avg_conf,
        warnings=warnings
    )



