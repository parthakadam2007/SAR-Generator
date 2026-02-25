from .ai_graph_tools import (
    detect_layering,
    detect_pass_through,
    detect_cross_border,
    detect_velocity_spike
)
from .explainablity_engine import generate_explanation


def run_full_investigation(case_id: str):

    # Run all tools deterministically
    tool_results = {
        "detect_layering": detect_layering(case_id),
        "detect_pass_through": detect_pass_through(case_id),
        "detect_cross_border": detect_cross_border(case_id),
        "detect_velocity_spike": detect_velocity_spike(case_id),
    }

    # Calculate risk score
    risk_score = 0
    triggered_patterns = []

    if tool_results["detect_layering"]["matches_found"] > 0:
        risk_score += 30
        triggered_patterns.append("detect_layering")

    if tool_results["detect_pass_through"]["matches_found"] > 0:
        risk_score += 20
        triggered_patterns.append("detect_pass_through")

    if tool_results["detect_cross_border"]["matches_found"] > 0:
        risk_score += 25
        triggered_patterns.append("detect_cross_border")

    if tool_results["detect_velocity_spike"]["matches_found"] > 0:
        risk_score += 15
        triggered_patterns.append("detect_velocity_spike")

    if risk_score >= 75:
        risk_level = "HIGH"
        recommendation = "STR strongly recommended"
    elif risk_score >= 40:
        risk_level = "MEDIUM"
        recommendation = "Manual review required"
    else:
        risk_level = "LOW"
        recommendation = "No immediate action"

    result = {
        "case_id": case_id,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "triggered_patterns": triggered_patterns,
        "tool_results": tool_results,
        "recommendation": recommendation
    }

    explanation = generate_explanation(result)

    return {
        "investigation_result": result,
        "explanation": explanation
    }