"""from fastapi import APIRouter
from app.contributions_store import contributions, stats
from fastapi.responses import PlainTextResponse






router = APIRouter(prefix="/dashboard", tags=["Dashboards"])

@router.get("/contributors", response_class=PlainTextResponse)
def contributor_dashboard():
    total = len(contributions)
    approved = sum(1 for c in contributions if c["status"] == "approved")
    pending = sum(1 for c in contributions if c["status"] == "pending")

    top = sorted(
        stats.items(),
        key=lambda x: x[1]["approved"],
        reverse=True
    )[:5]

    lines = [
        "🌍 Community Contributors Dashboard\n",
        f"Total Contributions: {total}",
        f"Approved Contributions: {approved}",
        f"Pending Review: {pending}\n",
        "🏆 Top Contributors"
    ]

    for i, (name, s) in enumerate(top, start=1):
        lines.append(f"{i}. {name} — {s['approved']} approved")

    lines.append("\n📈 Recent Contributions")
    for c in contributions[-10:]:
        lines.append(
            f"• {c['domain']} — {c['status'].capitalize()}"
        )

    return "\n".join(lines)"""
"""@router.get("/contributors", response_class=PlainTextResponse)
def contributor_dashboard():
    return (
        "🌍 Community Contributors Dashboard\n\n"
        "This page will show:\n"
        "- Top contributors\n"
        "- Approved contributions\n"
        "- Community impact\n\n"
        "Coming soon."
    )"""

