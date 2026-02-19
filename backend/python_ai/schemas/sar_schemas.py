from pydantic import BaseModel
from typing import List, Dict, Any,Literal
from datetime import date
from uuid import UUID

class RiskAssessment(BaseModel):
    risk_category: str
    alerts_triggered: List[str]
    inconsistencies: List[str]

class SubjectProfile(BaseModel):
    customer_id: UUID
    full_name: str
    dob: date
    pan: str
    aadhaar_last4: str
    occupation: str
    declared_annual_income: float
    address: str
    kyc_last_updated: date
    account_number: str
    account_type: Literal["Savings", "Current", "Business"]
    opened_date: date
    average_monthly_balance: float
    average_monthly_credit: float
    average_monthly_debit: float
    usual_transaction_pattern: str

class SARContent(BaseModel):
    sar_summary: str
    subject_profile: SubjectProfile
    risk_assessment: RiskAssessment
    suspicious_indicators: List[str]
    transaction_analysis: str
    narrative: str
    recommended_action: str

