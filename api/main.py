from fastapi import FastAPI
import torch
import numpy as np

from triage.risk_prioritizer import assign_priority
from explainability.llm_explainer import generate_explanation

app = FastAPI(title="Fraud Alert Triage API")

# ----------------------------
# Mock model inference function
# (Replace with real model later)
# ----------------------------
def predict_fraud_risk(features):
    # In a real system:
    # load model + scaler and run inference
    return 0.91  # mocked high-risk score


@app.post("/analyze-transaction")
def analyze_transaction(transaction: dict):
    """
    Analyze a transaction and return fraud risk, priority, and explanation.
    """

    risk_score = predict_fraud_risk(transaction.get("features", []))

    priority = assign_priority(
        risk_score=risk_score,
        amount=transaction.get("amount", 0),
        velocity_flag=transaction.get("velocity_flag", False),
        geo_mismatch=transaction.get("geo_mismatch", False)
    )

    explanation = generate_explanation(
        transaction=transaction,
        risk_score=risk_score,
        priority=priority
    )

    return {
        "risk_score": round(risk_score, 3),
        "priority": priority,
        "explanation": explanation
    }
