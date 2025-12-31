import re


def enforce_terminology(
    text: str,
    approved_terms: dict
) -> tuple[str, list[str]]:
    """
    Enforces approved terminology.
    Replaces variants with approved forms.
    """
    warnings = []

    for src, tgt in approved_terms.items():
        pattern = re.compile(rf"\b{re.escape(src)}\b", re.IGNORECASE)
        if pattern.search(text):
            text = pattern.sub(tgt, text)
        else:
            warnings.append(f"MISSING_APPROVED_TERM:{src}")

    return text, warnings
