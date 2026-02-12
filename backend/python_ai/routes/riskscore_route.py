# risk_routes.py

from fastapi import APIRouter
from services.riskscore_service import calculate_risk

router = APIRouter()


@router.post("/evaluate-risk")
async def evaluate_risk(case_data: dict):
    result = calculate_risk(case_data)
    return {
        "status": "success",
        "result": result
    }
