# Terminology Governance

This system ensures **one concept = one approved term**.

---

## Why Governance Matters

In safety-critical contexts, inconsistent terminology can cause:
- Medical errors
- Legal confusion
- Loss of public trust

---

## Workflow

1. **Propose**
   - Anyone may propose a term
   - Terms are NOT enforced until approved

2. **Review**
   - Human reviewer evaluates accuracy, clarity, and safety

3. **Approve**
   - Approved terms become mandatory in the domain

---

## Conflict Rules

A proposal is rejected if:
- A source term already maps to a different target
- A target term already represents a different source
- An approved term would be contradicted

Conflict responses return HTTP 409.

---

## Authority

- Approval authority is domain-specific
- All approvals are logged and auditable
- Silent overrides are not permitted

---

## Public Transparency

Approved terminology is publicly accessible via the API.
