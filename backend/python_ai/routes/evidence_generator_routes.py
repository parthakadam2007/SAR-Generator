from fastapi import APIRouter
from services.evidence_generator import generate_evidence
from services.riskscore_service import calculate_risk

evidence_router = APIRouter()

@evidence_router.post("/generate_evidence")
async def generate_evidences(case_data: dict):
    risk = calculate_risk(case_data)
    evidence_output = generate_evidence(case_data, risk)
    return{
        "status": "success",
        "result": evidence_output
    }