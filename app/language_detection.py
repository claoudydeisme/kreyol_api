from langdetect import detect_langs


def detect_language(text: str) -> tuple[str, float]:
    """
    Detects language and returns (language_code, confidence)
    """
    try:
        langs = detect_langs(text)
        best = langs[0]
        code = "ht" if best.lang in {"ht", "fr"} else "en"
        return code, best.prob
    except Exception:
        return "unknown", 0.0
