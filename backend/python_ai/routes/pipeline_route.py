from fastapi import APIRouter
from services.riskscore_service import calculate_risk
from services.evidence_generator import generate_evidence

pipeline_router = APIRouter()

# Adjustable threshold
RISK_EVIDENCE_THRESHOLD = 50


@pipeline_router.post("/risk-pipeline")
async def risk_pipeline(case_data: dict):

    # Step 1 — Risk scoring
    risk_result = calculate_risk(case_data)
    score = risk_result["risk_score"]

    response = {
        "status": "success",

        # ✅ echo original input
        "input": case_data,

        # risk result
        "risk": risk_result,

        # decision config
        "threshold": RISK_EVIDENCE_THRESHOLD,

        # evidence section
        "evidence_generated": False,
        "evidence": []
    }

    # Step 2 — Threshold decision
    if score >= RISK_EVIDENCE_THRESHOLD:
        evidence = generate_evidence(case_data, risk_result)
        response["evidence_generated"] = True
        response["evidence"] = evidence

    return response
