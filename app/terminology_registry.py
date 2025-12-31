from typing import Dict, List, Optional
from app.terminology_models import TermEntry
from datetime import datetime
from uuid import uuid4
from app.terminology_models import TermEntry


class TerminologyRegistry:
    def __init__(self):
        self._terms: Dict[str, List[TermEntry]] = {}

    def propose_term(self, data):
        """
            entry = TermEntry(
            id=str(uuid4()),
            domain=data.domain,
            source_language=data.source_language,
            target_language=data.target_language,
            source_term=data.source_term,
            target_term=data.target_term,
            approved=False,
            created_by=data.created_by,
            created_at=datetime.utcnow()
            )
            self._terms.set
        """
        # When someone wants to propose a new term, we have to check the congruence and see if its not going to overwrite an existing response for that term or contradict a verified one
        conflict = self.detect_conflict(
        data.domain,
        data.source_language,
        data.target_language,
        data.source_term,
        data.target_term
        )

        if conflict:
            raise ValueError(conflict)

        entry = TermEntry(
            id=str(uuid4()),
            domain=data.domain,
            source_language=data.source_language,
            target_language=data.target_language,
            source_term=data.source_term,
            target_term=data.target_term,
            approved=False,
            created_by=data.created_by,
            created_at=datetime.utcnow()
        )

        self._terms.setdefault(entry.domain, []).append(entry)
        return entry

    

    def approve_term(self, term_id: str, reviewer: str):
        for domain_terms in self._terms.values():
            for term in domain_terms:
                if term.id == term_id:
                    term.approved = True
                    term.reviewed_by = reviewer
                    term.reviewed_at = datetime.utcnow()
                    return term
        return None
    # 🌍 Used by the public API 
    def get_approved_terms_entries(self, domain: str):
        return [
            t for t in self._terms.get(domain, [])
            if t.approved
        ]

    def add_term(self, entry: TermEntry):
        self._terms.setdefault(entry.domain, []).append(entry)
    # 🔒 Used by the translator 
    def get_approved_terms(
        self,
        domain: str,
        source_language: str,
        target_language: str
    ) -> Dict[str, str]:
        approved = {}
        for term in self._terms.get(domain, []):
            if (
                term.approved
                and term.source_language == source_language
                and term.target_language == target_language
            ):
                approved[term.source_term.lower()] = term.target_term
        return approved
    #deal with different conflict detection
    def detect_conflict(
        self,
        domain: str,
        source_language: str,
        target_language: str,
        source_term: str,
        target_term: str
    ) -> Optional[str]:
        """
        Returns a conflict reason string if conflict exists, otherwise None.
        """
        for term in self._terms.get(domain, []):
            if (
                term.source_language == source_language
                and term.target_language == target_language
            ):
                # Conflict A: same source, different target
                #"blood pressure" → "tansyon"
                #"blood pressure" → "presyon san"

                if (
                    term.source_term.lower() == source_term.lower()
                    and term.target_term.lower() != target_term.lower()
                ):
                    return "SOURCE_TERM_CONFLICT"

                # Conflict B: same target, different source
                #"blood pressure" → "tansyon"
                #"blood sugar"   → "tansyon"

                if (
                    term.target_term.lower() == target_term.lower()
                    and term.source_term.lower() != source_term.lower()
                ):
                    return "TARGET_TERM_CONFLICT"

        return None
