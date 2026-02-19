import os
import json
import traceback
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from schemas.sar_schemas import SARContent

load_dotenv()

# -------------------------------------------------------
# Debug Utility
# -------------------------------------------------------

def debug_log(message):
    print(f"[DEBUG] {message}")

# -------------------------------------------------------
# Gemini LLM Setup with Validation
# -------------------------------------------------------

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise EnvironmentError("❌ GOOGLE_API_KEY not found in environment variables.")

debug_log("API key loaded successfully.")

try:
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
        google_api_key=GOOGLE_API_KEY
    )
    structured_llm = llm.with_structured_output(SARContent)
    debug_log("Gemini model initialized successfully.")
except Exception as e:
    raise RuntimeError(f"❌ Failed to initialize Gemini model: {str(e)}")

# -------------------------------------------------------
# Strict SAR Prompt
# -------------------------------------------------------

SAR_PROMPT = """
You are a financial compliance SAR writer.

You MUST generate a Suspicious Activity Report in STRICT JSON format.

Rules:
- Use only provided facts
- No speculation
- No emotional language
- No assumptions
- Regulatory tone
- Chronological narrative
- Evidence-backed statements only
- Output MUST be valid JSON
- Do NOT include markdown
- Do NOT include explanation

Return format:

{{
  "sar_summary": "",
  "subject_profile": {{}},
  "risk_assessment": {{}},
  "suspicious_indicators": [],
  "transaction_analysis": "",
  "narrative": "",
  "recommended_action": ""
}}

Input Case Data:
{case_data}

Evidence:
{evidence}
"""

prompt_template = ChatPromptTemplate.from_template(SAR_PROMPT)

# -------------------------------------------------------
# SAR Generator with Full Error Handling
# -------------------------------------------------------

def generate_sar(case_data: dict, evidence: list, verbose=True):

    if verbose:
        debug_log("Starting SAR generation...")

    if not isinstance(case_data, dict):
        return {"error": "case_data must be a dictionary"}
    if not isinstance(evidence, list):
        return {"error": "evidence must be a list"}

    try:
        chain = prompt_template | structured_llm

        if verbose:
            debug_log("Invoking Gemini with structured schema enforcement...")

        response = chain.invoke({
            "case_data": json.dumps(case_data, indent=2),
            "evidence": json.dumps(evidence, indent=2)
        })

        if verbose:
            debug_log("Structured SAR generated successfully.")

        # response is already validated Pydantic object
        return response.model_dump()

    except Exception as e:
        error_trace = traceback.format_exc()

        debug_log("❌ Structured SAR generation failed")
        debug_log(error_trace)

        return {
            "error": "SAR generation failed",
            "details": str(e),
            "trace": error_trace
        }
