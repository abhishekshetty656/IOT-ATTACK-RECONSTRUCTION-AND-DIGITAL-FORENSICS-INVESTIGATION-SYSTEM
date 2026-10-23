def calculate_risk_score(severity, confidence):
    """Return a risk score for an IoT forensic event.
    severity: whole number from 1 to 10
    confidence: number from 0 to 1
    """
    if not isinstance(severity, int) or not 1 <= severity <= 10:
        raise ValueError("severity must be an integer between 1 and 10")
    if not 0 <= confidence <= 1:
        raise ValueError("confidence must be between 0 and 1")
    return round(severity * confidence * 10, 2)
