
---

# Linguistic Rules & Guarantees

This API enforces **standard Haitian Creole** and safe English.

---

## Haitian Creole Rules (Non-Negotiable)

- Standard Haitian Creole orthography only
- No French grammar structures
- No English word leakage
- Verbs remain invariant
- Tense expressed with markers:
  - ap (ongoing)
  - te (past)
  - pral (future)
- Articles follow nouns:
  - liv la
  - timoun yo

---

## Translation Philosophy

- Semantic accuracy over literal translation
- Preserve meaning, not syntax
- Prefer explicitness over ambiguity
- Avoid idioms in sensitive domains

---

## Domain Safety

In healthcare, government, and education:
- No paraphrasing of key terms
- No metaphors
- No implied advice

---

## Output Guarantees

- Grammatically correct
- Readable aloud (TTS-safe)
- Appropriate for non-technical audiences
