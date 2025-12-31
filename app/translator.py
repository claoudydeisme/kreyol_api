from app.models.model import neural_translate
from app.domain_terms import enforce_domain_terms
from app.terminology_registry import TerminologyRegistry
from app.terminology_enforcer import enforce_terminology
from app.datasets.dataset_store import parallel_dataset



def lookup_parallel_dataset(
    text: str,
    source_language: str,
    target_language: str,
    domain: str
):
    for pair in parallel_dataset.filter(
        source_language=source_language,
        target_language=target_language,
        domain=domain
    ):
        if pair["source"].lower().strip() == text.lower().strip():
            return pair["target"]

    return None


def translate_text(
    text: str,
    source_language: str,
    target_language: str,
    domain: str
) -> tuple[str, float]:
    
    # 1️⃣ Exact dataset lookup FIRST (human-verified)
    exact = lookup_parallel_dataset(
        text,
        source_language,
        target_language,
        domain
    )

    if exact:
        return exact.strip(), 1.0
    
    
    # 2️⃣ Neural translation fallback
    translation = neural_translate(text, source_language, target_language)
    registry = TerminologyRegistry()

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


#print("DATASET INSTANCE ID (translator):", id(parallel_dataset))
#print("DATASET SIZE (translator):", len(parallel_dataset.pairs))

