from fastapi import APIRouter
from services.riskscore_service import calculate_risk
from services.evidence_generator import generate_evidence
from services.sar_ai_service import generate_sar

sar_router = APIRouter()

RISK_EVIDENCE_THRESHOLD = 50

@sar_router.post("/sar-pipeline")
async def sar_pipeline(case_data: dict):

    # Step 1 — risk scoring
    risk_result = calculate_risk(case_data)
    score = risk_result["risk_score"]

    response = {
        "status": "success",
        "input": case_data,
        "risk": risk_result,
        "threshold": RISK_EVIDENCE_THRESHOLD,
        "evidence_generated": False,
        "evidence": [],
        "sar_generated": False,
        "sar": {}
    }

    # Step 2 — evidence generation
    if score >= RISK_EVIDENCE_THRESHOLD:
        evidence = generate_evidence(case_data, risk_result)
        response["evidence_generated"] = True
        response["evidence"] = evidence

        # Step 3 — AI SAR generation
        sar = generate_sar(case_data, evidence)
        response["sar_generated"] = True
        response["sar"] = sar

    return response

