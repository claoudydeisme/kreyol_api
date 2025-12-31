from app.document_parser import split_document
from app.translator import translate_text
from app.term_memory import TermMemory


def translate_long_document(
    text: str,
    source_language: str,
    target_language: str,
    domain: str
):
    sections = split_document(text)
    term_memory = TermMemory()

    translated_sections = []
    confidences = []
    warnings = []

    for sec in sections:
        translated, confidence = translate_text(
            sec["source"],
            source_language,
            target_language,
            domain
        )

        translated = term_memory.enforce(translated)

        # Register terminology for consistency
        if len(sec["source"].split()) <= 5:
            term_memory.register(sec["source"], translated)

        translated_sections.append({
            "type": sec["type"],
            "source": sec["source"],
            "translation": translated,
            "confidence": confidence
        })

        confidences.append(confidence)

    avg_conf = sum(confidences) / len(confidences)

    return translated_sections, avg_conf, warnings
