import re
from enum import Enum
from typing import List, Dict


class Severity(str, Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"

def enforce_creole_rules(text: str) -> list[str]:
    warnings = []

    forbidden_patterns = ["est ", "être ", " le ", " la ", "parce que", "au moins", "en tout cas", "bien que"]
    for p in forbidden_patterns:
        if p in text.lower():
            warnings.append("POTENTIAL_FRENCH_STRUCTURE")

    return warnings


#def simplify_if_low_confidence(text: str) -> str:
    #return "Fraz la pa klè. Mwen bay yon vèsyon ki pi dirèk."


def enforce_creole_grammar(text: str) -> list[str]:
    warnings = []
    """
    Returns a list of grammar issues with severity.
    Non-destructive: does NOT modify text.
    """
    # French determiners before noun (illegal)
    if re.search(r"\b(le|la|les)\s+\w+", text.lower()):
        warnings.append({
            "code": "FRENCH_GRAMMAR_PATTERN",
            "severity": Severity.CRITICAL
        })

    # ❌ English auxiliary verbs leaking
    if re.search(r"\b(is|are|was|were|has|have)\b", text.lower()):
        warnings.append({
            "code": "ENGLISH_VERB_LEAK",
            "severity": Severity.CRITICAL
        })

    # Missing tense marker heuristic
    if re.search(r"\bmwen\s+\w+\b", text.lower()):
        if not any(marker in text.lower() for marker in [" ap ", " te ", " pral "]):
            warnings.append({
                "code": "MISSING_TENSE_MARKER",
                "severity": Severity.WARNING
            })

    # ⚠ Article before noun (very common error)
    if re.search(r"\b(la|yo)\s+\w+", text.lower()):
        warnings.append({
            "code": "ARTICLE_POSITION_SUSPECT",
            "severity": Severity.WARNING
        })

    # ℹ Long sentence risk (clarity)
    if len(text.split()) > 30:
        warnings.append({
            "code": "LONG_SENTENCE_POSSIBLE_AMBIGUITY",
            "severity": Severity.INFO
        })

    return warnings

def should_simplify(issues: List[Dict]) -> bool:
    """

    
    Determines if output must be simplified.
    """
    return any(i["severity"] == Severity.CRITICAL for i in issues)


#def simplify_creole(text: str) -> str:
    #return (
        #"Fraz la pa klè. "
        #"Mwen bay yon tradiksyon ki pi dirèk ak pi senp."
    #)
