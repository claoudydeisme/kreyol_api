import re
from typing import Dict, List


CREOLE_TENSE_PARTICLES = {"ap", "te", "pral"}
FORBIDDEN_FRENCH_PATTERNS = [
    r"\bje\b", r"\btu\b", r"\bil\b", r"\belle\b",
    r"\bnous\b", r"\bvous\b", r"\bils\b",
    r"\bêtre\b", r"\bavoir\b"
]

FORBIDDEN_ENGLISH_WORDS = {
    "the", "and", "is", "are", "you", "have", "with"
}

COMMON_CONTRACTION_ERRORS = {
    r"santi mwen": "santi m",
    r"pale mwen": "pale m",
    r"di mwen": "di m"
}

UNSAFE_MEDICAL_ASSUMPTIONS = [
    r"medikaman an ba ou",
    r"sa lakoz",
    r"sa fè ou"
]


def lint_creole_sentence(
    text: str,
    row_id: str,
    row_num: int
) -> List[Dict]:
    issues = []

    lowered = text.lower()

    # 1️⃣ English leakage
    for word in FORBIDDEN_ENGLISH_WORDS:
        if re.search(rf"\b{word}\b", lowered):
            issues.append({
                "severity": "CRITICAL",
                "code": "ENGLISH_LEAKAGE",
                "row": row_num,
                "id": row_id,
                "message": f"English word '{word}' found"
            })

    # 2️⃣ French leakage
    for pattern in FORBIDDEN_FRENCH_PATTERNS:
        if re.search(pattern, lowered):
            issues.append({
                "severity": "CRITICAL",
                "code": "FRENCH_LEAKAGE",
                "row": row_num,
                "id": row_id,
                "message": f"French pattern '{pattern}' found"
            })

    # 3️⃣ Verb conjugation detection (very conservative)
    if re.search(r"\b(ais|ait|aient|ons|ez|ent)\b", lowered):
        issues.append({
            "severity": "ERROR",
            "code": "VERB_CONJUGATION",
            "row": row_num,
            "id": row_id,
            "message": "Possible verb conjugation detected"
        })

    # 4️⃣ Contraction enforcement
    for bad, good in COMMON_CONTRACTION_ERRORS.items():
        if re.search(bad, lowered):
            issues.append({
                "severity": "WARNING",
                "code": "CONTRACTION_MISSING",
                "row": row_num,
                "id": row_id,
                "message": f"Use '{good}' instead of '{bad}'"
            })

    # 5️⃣ Unsafe medical assumptions
    for pattern in UNSAFE_MEDICAL_ASSUMPTIONS:
        if re.search(pattern, lowered):
            issues.append({
                "severity": "CRITICAL",
                "code": "MEDICAL_ASSUMPTION",
                "row": row_num,
                "id": row_id,
                "message": "Medical causality assumed"
            })

    # 6️⃣ Speech safety (symbols & abbreviations)
    if re.search(r"\b\d+mg\b|\bml\b", lowered):
        issues.append({
            "severity": "WARNING",
            "code": "SPEECH_UNSAFE_ABBREVIATION",
            "row": row_num,
            "id": row_id,
            "message": "Avoid abbreviations for speech output"
        })

    return issues
