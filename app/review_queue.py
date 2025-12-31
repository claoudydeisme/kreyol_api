from datetime import datetime


REVIEW_QUEUE = []


def flag_for_human_review(
    source_text: str,
    translated_text: str,
    issues: list,
    domain: str
):
    REVIEW_QUEUE.append({
        "source": source_text,
        "translation": translated_text,
        "issues": issues,
        "domain": domain,
        "timestamp": datetime.utcnow().isoformat()
    })
