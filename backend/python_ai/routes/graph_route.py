from fastapi import APIRouter, HTTPException
from services.neo4j_service import insert_case_data

from services.case_analysis_service import analyze_case


router = APIRouter()

@router.post("/ingest-case")
async def ingest_case(case_json: dict):

    result = insert_case_data(case_json)

    return result




@router.get("/case/{case_id}/analysis")
async def case_analysis(case_id: str):

    result = analyze_case(case_id)

    if not result:
        raise HTTPException(status_code=404, detail="Case not found")

    return result