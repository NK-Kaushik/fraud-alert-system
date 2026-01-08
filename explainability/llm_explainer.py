def generate_explanation(transaction, risk_score, priority):
    """
    Generate a compliance-safe explanation for fraud analysts.
    """

    explanation = (
        f"This transaction was flagged for review with a {priority} priority. "
        f"The fraud risk model assigned a risk score of {risk_score:.2f}. "
    )

    if transaction["amount"] > 500:
        explanation += "The transaction amount is higher than typical spending behavior. "

    if transaction.get("velocity_flag"):
        explanation += "Multiple rapid transactions were detected in a short time window. "

    if transaction.get("geo_mismatch"):
        explanation += "The transaction location differs from recent customer activity. "

    explanation += (
        "These indicators suggest elevated risk, but do not confirm fraud. "
        "Manual review is recommended before taking action."
    )

    return explanation
