from llm_explainer import generate_explanation

sample_txn = {
    "amount": 1200,
    "velocity_flag": True,
    "geo_mismatch": False
}

explanation = generate_explanation(
    transaction=sample_txn,
    risk_score=0.91,
    priority="HIGH"
)

print(explanation)
