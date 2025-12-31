# API Reference

Base URL: - 
** Run this in your server if reading this and no base url has been provided yet **


---

## POST /translate

Translate short text (≤ 300 words).

### Request
```json
{
  "text": "I am going to the hospital tomorrow.",
  "source_language": "en",
  "target_language": "ht",
  "domain": "healthcare"
}
### Response
{
  "translation": "Mwen pral ale lopital demen.",
  "confidence": 0.96,
  "warnings": []
}


POST /translate/long
Translate long documents (> 300 words) with structure preserved.
Response Structure in json
{
  "sections": [
    {
      "type": "heading | paragraph | list",
      "source": "...",
      "translation": "...",
      "confidence": 0.94
    }
  ],
  "average_confidence": 0.93
}


*** Terminology Governance ***
POST /terminology/propose
Propose a new term (unapproved).

POST /terminology/approve
Approve a term (restricted access).

GET /terminology/{domain}
List approved terms (public, read-only).



Error Codes
Code	Meaning
400	Invalid request
409	Terminology conflict
413	Text too long
500	Internal error