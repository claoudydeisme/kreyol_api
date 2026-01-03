#from app.models.model import neural_translate
from app.domain_terms import enforce_domain_terms
from app.terminology_registry import TerminologyRegistry
from app.terminology_enforcer import enforce_terminology
from app.datasets.registry_data import get_dataset


def lookup_parallel_dataset(
    text: str,
    source_language: str,
    target_language: str,
    domain: str
):
    """
    Look up translation in parallel dataset.
    Supports bidirectional search - if direct match not found,
    searches in reverse direction.
    """
    try:
        dataset = get_dataset(domain)
    except KeyError:
        return None
    
    # Normalize input text - lowercase, strip whitespace, remove extra spaces
    normalized_text = ' '.join(text.lower().strip().split())
    
    # 1️⃣ DIRECT SEARCH: source_language → target_language
    for pair in dataset.filter(
        source_language=source_language,
        target_language=target_language,
        domain=domain
    ):
        # Normalize CSV data the same way
        normalized_source = ' '.join(pair["source"].lower().strip().split())
        if normalized_source == normalized_text:
            return pair["target"].strip()
    
    # 2️⃣ REVERSE SEARCH: Check if input matches target in reverse direction
    # Example: User asks en→ht for "hello", but we have ht→en: "bonjou" → "hello"
    # So we search where target_language=en matches "hello", and return the source
    for pair in dataset.filter(
        source_language=target_language,  # Swap: search where target is now source
        target_language=source_language,  # Swap: search where source is now target
        domain=domain
    ):
        # Normalize CSV data
        normalized_target = ' '.join(pair["target"].lower().strip().split())
        # If the target (in reverse direction) matches our input text
        if normalized_target == normalized_text:
            # Return the source (in reverse direction) as our translation
            return pair["source"].strip()
    
    # No match found in either direction
    return None


def translate_text(
    text: str,
    source_language: str,
    target_language: str,
    domain: str
) -> tuple[str, float]:
    """
    Translate text using parallel dataset with bidirectional search.
    
    Args:
        text: Text to translate
        source_language: Source language code (en/ht)
        target_language: Target language code (en/ht)
        domain: Domain (general/healthcare/education)
    
    Returns:
        tuple: (translation, confidence)
    """
    
    # 1️⃣ Dataset lookup with bidirectional search
    translation = lookup_parallel_dataset(
        text,
        source_language,
        target_language,
        domain
    )
    
    if translation:
        return translation.strip(), 1.0
    
    # 2️⃣ Fallback message
    return 'No translation available yet', 0.5
    
    # 3️⃣ Future: Neural translation fallback
    # translation = neural_translate(text, source_language, target_language)
    # registry = TerminologyRegistry()
    # ... (neural translation logic)
    
    # 2️⃣ Neural translation fallback
    #translation = neural_translate(text, source_language, target_language)
    #registry = TerminologyRegistry()

    """ 
    approved_terms = registry.get_approved_terms(
    domain,
    source_language,
    target_language
    )

    translation, term_warnings = enforce_terminology(
    translation,
    approved_terms
    )


    direction = f"{source_language}→{target_language}"

    translation = enforce_domain_terms(
        translation,
        domain,
        direction
    )
        
    
    
    warnings = []
    warnings.extend(term_warnings)

    # Confidence heuristic (deterministic & auditable)
    confidence = 0.90
    if len(translation.split()) < len(text.split()) * 0.6:
        confidence -= 0.2

    return translation.strip(), max(confidence, 0.0)
    """

#print("DATASET INSTANCE ID (translator):", id(parallel_dataset))
#print("DATASET SIZE (translator):", len(parallel_dataset.pairs))

