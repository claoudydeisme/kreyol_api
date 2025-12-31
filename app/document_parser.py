import re


def split_document(text: str) -> list[dict]:
    """
    Splits document into structured sections:
    headings, paragraphs, lists.
    """
    sections = []
    blocks = re.split(r"\n{2,}", text)

    for block in blocks:
        block = block.strip()
        if not block:
            continue

        if block.isupper() and len(block.split()) < 10:
            section_type = "heading"
        elif re.match(r"^[-•*]\s+", block):
            section_type = "list"
        else:
            section_type = "paragraph"

        sections.append({
            "type": section_type,
            "source": block
        })

    return sections
