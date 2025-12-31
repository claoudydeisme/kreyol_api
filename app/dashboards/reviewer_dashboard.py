"""from fastapi import APIRouter, Depends
from app.security import require_reviewer
from app.contributions_store import contributions, stats
from fastapi.responses import PlainTextResponse


router = APIRouter(prefix="/dashboard", tags=["Dashboards"])

@router.get("/reviewers", response_class=PlainTextResponse)
def reviewer_dashboard(
    reviewer: str = Depends(require_reviewer)
):
    pending = [c for c in contributions if c["status"] == "pending"]

    lines = [
        "🛡️ Reviewer Dashboard\n",
        f"Pending Reviews: {len(pending)}\n",
        "📥 Review Queue"
    ]

    for c in pending[:20]:
        lines.append(f"• {c['domain']} — Pending")

    lines.append("\n👤 Reviewer Activity")
    for name, s in stats.items():
        if s["approved"] > 0:
            lines.append(f"• {name} — {s['approved']} approvals")

    return "\n".join(lines)
"""