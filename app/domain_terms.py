
DOMAIN_TERMS = {
    "healthcare": {
        "hospital": "lopital",
        "medication": "medikaman",
        "appointment": "randevou",
        "emergency": "ijans",
        "blood pressure": "tansyon"
    },
    "education": {},
    "government": {},
    "general": {}
    }


def enforce_domain_terms(text: str, domain: str, direction: str) -> str:
    """
    Ensures locked terminology is used.
    direction: en→ht or ht→en
    """
    

    if domain not in DOMAIN_TERMS:
        return text

    for src, tgt in DOMAIN_TERMS[domain].items():
        if direction == "en→ht":
            text = text.replace(src, tgt)
        else:
            text = text.replace(tgt, src)

    return text
