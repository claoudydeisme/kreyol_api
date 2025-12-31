import hashlib
from datetime import datetime


def log_translation(source: str, target: str, confidence: float, domain: str):
    record = {
        "source_hash": hashlib.sha256(source.encode()).hexdigest(),
        "target_hash": hashlib.sha256(target.encode()).hexdigest(),
        "confidence": confidence,
        "domain": domain,
        "timestamp": datetime.utcnow().isoformat()
    }

    # Replace with DB / queue
    print(record)
