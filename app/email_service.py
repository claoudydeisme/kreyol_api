# email_service.py
# Add this file to your app/ directory

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Dict, Any, Optional
import os
from datetime import datetime

router = APIRouter()

# Email configuration - UPDATE THESE WITH YOUR CREDENTIALS
SMTP_SERVER = "smtp.gmail.com"  # Gmail SMTP server
SMTP_PORT = 587  # TLS port
SENDER_EMAIL = os.getenv("SENDER_EMAIL", "claroossdeisme@gmail.com")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD", "fuqt wcix kbtu epvk")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL", "psechein@gmail.com")

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

# Email sending function
def send_email(to_email: str, subject: str, body: str, is_html: bool = False):
    """Send email via Gmail SMTP"""
    try:
        # Create message
        msg = MIMEMultipart('alternative')
        msg['From'] = SENDER_EMAIL
        msg['To'] = to_email
        msg['Subject'] = subject
        msg['Date'] = datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z")
        
        # Attach body
        if is_html:
            msg.attach(MIMEText(body, 'html'))
        else:
            msg.attach(MIMEText(body, 'plain'))
        
        # Connect to SMTP serve
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")

# Feedback endpoint
@router.post("/send-feedback")
async def send_feedback_email(request: FeedbackRequest):
    """Send user feedback via email"""
    
    # Format feedback email
    feedback = request.feedback_data
    
    email_body = f"""
=================================================================
KREYOLAPI USER FEEDBACK
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

Original Text: (Not captured for privacy)
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
    
    email_body += """
=================================================================
"""
    
    # Send email
    send_email(
        to_email=request.to_email,
        subject=request.subject,
        body=email_body
    )
    
    return {"status": "success", "message": "Feedback sent successfully"}

# Contribution endpoint
@router.post("/send-contribution")
async def send_contribution_email(request: ContributionRequest):
    """Send translation contribution via email"""
    
    # Send email with contribution details
    send_email(
        to_email=request.to_email,
        subject=request.subject,
        body=request.contribution_note
    )
    
    return {
        "status": "success", 
        "message": "Contribution sent successfully",
        "contribution_id": request.csv_data.get('id')
    }

# Health check endpoint
@router.get("/email-service/health")
async def email_health():
    """Check if email service is configured"""
    configured = (
        SENDER_EMAIL != "your-email@gmail.com" and 
        SENDER_PASSWORD != "your-app-password"
    )
    return {
        "status": "configured" if configured else "not_configured",
        "smtp_server": SMTP_SERVER,
        "sender_email": SENDER_EMAIL if configured else "not_set"
    }
#http://localhost:8080/demo.html