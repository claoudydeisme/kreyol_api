# email_service.py
# Using Resend API (works on Railway - no SMTP)

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Dict, Any
import os
import httpx

router = APIRouter()

# Email configuration
RESEND_API_KEY ="re_gr49c4Hz_7JtJLSzWVi62igojH7F321iD"
SENDER_EMAIL ="contact@kreyolapi.org"
RECEIVER_EMAIL ="claoudy.deisme@estudiantes.unahur.edu.ar"

# Models
class FeedbackRequest(BaseModel):
    to_email: EmailStr
    subject: str
    feedback_data: Dict[str, Any]

class ContributionRequest(BaseModel):
    to_email: EmailStr
    subject: str
    contribution_note: str
    csv_data: Dict[str, str]
    contributor_name: str

# Send email via Resend HTTP API
async def send_email_resend(to_email: str, subject: str, body: str):
    """Send email via Resend HTTP API (works on Railway)"""
    
    if not RESEND_API_KEY:
        raise HTTPException(
            status_code=500, 
            detail="RESEND_API_KEY not configured"
        )
    
    try:
        url = "https://api.resend.com/emails"
        
        headers = {
            "Authorization": f"Bearer {RESEND_API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "from": SENDER_EMAIL,
            "to": [to_email],
            "subject": subject,
            "text": body
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                url, 
                json=payload, 
                headers=headers, 
                timeout=10.0
            )
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Email sent to {to_email}, ID: {result.get('id')}")
            return True
        else:
            print(f"❌ Resend error: {response.status_code} - {response.text}")
            raise HTTPException(
                status_code=500,
                detail=f"Email failed: {response.status_code}"
            )
            
    except Exception as e:
        print(f"❌ Email error: {str(e)}")
        raise HTTPException(
            status_code=500, 
            detail=f"Failed to send email: {str(e)}"
        )

@router.post("/send-feedback")
async def send_feedback_email(request: FeedbackRequest):
    """Send user feedback via email"""
    
    feedback = request.feedback_data
    
    email_body = f"""
=================================================================
VOKAL KREYÒL USER FEEDBACK
=================================================================

Feedback Type: {feedback.get('type', 'N/A').upper()}
Timestamp: {feedback.get('timestamp', 'N/A')}

-----------------------------------------------------------------
TRANSLATION DETAILS:
-----------------------------------------------------------------
"""
    
    if feedback.get('translation'):
        trans = feedback['translation']
        email_body += f"""
Source Language: {trans.get('source_language', 'N/A')}
Target Language: {trans.get('target_language', 'N/A')}
Domain: {trans.get('domain', 'N/A')}
Confidence: {trans.get('confidence', 'N/A')}

Translation: {trans.get('translation', 'N/A')}
Warnings: {', '.join(trans.get('warnings', [])) if trans.get('warnings') else 'None'}
"""
    
    if feedback.get('comment'):
        email_body += f"""
-----------------------------------------------------------------
USER COMMENT:
-----------------------------------------------------------------
{feedback['comment']}
"""
    
    email_body += "\n================================================================="
    
    await send_email_resend(
        to_email=request.to_email,
        subject=request.subject,
        body=email_body
    )
    
    return {"status": "success", "message": "Feedback sent successfully"}

@router.post("/send-contribution")
async def send_contribution_email(request: ContributionRequest):
    """Send translation contribution via email"""
    
    await send_email_resend(
        to_email=request.to_email,
        subject=request.subject,
        body=request.contribution_note
    )
    
    return {
        "status": "success",
        "message": "Contribution sent successfully",
        "contribution_id": request.csv_data.get('id')
    }

@router.get("/email-service/health")
async def email_health():
    """Check if email service is configured"""
    configured = bool(RESEND_API_KEY and RESEND_API_KEY != "")
    
    return {
        "status": "configured" if configured else "not_configured",
        "email_service": "Resend HTTP API",
        "sender_email": SENDER_EMAIL if configured else "not_set",
        "note": "Railway blocks SMTP, using HTTP API"
    }