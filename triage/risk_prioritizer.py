def assign_priority(risk_score, amount, velocity_flag=False, geo_mismatch=False):
    """
    Convert fraud risk score into analyst priority.
    """

    # High confidence fraud signals
    if risk_score >= 0.85:
        return "HIGH"

    # Medium confidence with contextual risk
    if risk_score >= 0.6 and (amount > 500 or velocity_flag or geo_mismatch):
        return "MEDIUM"

    # Low risk
    return "LOW"
