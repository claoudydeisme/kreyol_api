import re


def normalize_text(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)  # strip HTML
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def word_count(text: str) -> int:
    return len(text.split())
