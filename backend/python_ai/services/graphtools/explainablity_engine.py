from datetime import datetime

def format_datetime(dt):
    if hasattr(dt, "iso_format"):
        return dt.iso_format()
    return str(dt)


def generate_explanation(investigation_result: dict):

    explanation_lines = []

    case_id = investigation_result["case_id"]
    risk_score = investigation_result["risk_score"]
    risk_level = investigation_result["risk_level"]

    explanation_lines.append(
        f"Case {case_id} was assessed as {risk_level} risk "
        f"with a total risk score of {risk_score}."
    )

    tool_results = investigation_result.get("tool_results", {})

    # ---------------- LAYERING ----------------
    layering = tool_results.get("detect_layering")
    if layering and layering["matches_found"] > 0:

        explanation_lines.append(
            f"\nLayering activity detected ({layering['matches_found']} instances):"
        )

        unique_paths = set()

        for item in layering["details"]:
            key = (item["destination"], item["hop_count"], item["total_amount"])
            if key in unique_paths:
                continue
            unique_paths.add(key)

            explanation_lines.append(
                f"- Funds moved from {item['source']} to {item['destination']} "
                f"over {item['hop_count']} hops "
                f"with total amount ₹{item['total_amount']:,}."
            )

    # ---------------- PASS THROUGH ----------------
    pass_through = tool_results.get("detect_pass_through")
    if pass_through and pass_through["matches_found"] > 0:

        explanation_lines.append(
            f"\nPass-through behavior detected ({pass_through['matches_found']} instances):"
        )

        seen = set()

        for item in pass_through["details"]:
            key = (item["mirrored_amount"], str(item["incoming_time"]))
            if key in seen:
                continue
            seen.add(key)

            explanation_lines.append(
                f"- ₹{item['mirrored_amount']:,} received at "
                f"{format_datetime(item['incoming_time'])} "
                f"and transferred out at "
                f"{format_datetime(item['outgoing_time'])}."
            )

    # ---------------- CROSS BORDER ----------------
    cross_border = tool_results.get("detect_cross_border")
    if cross_border and cross_border["matches_found"] > 0:

        explanation_lines.append(
            f"\nCross-border transfers detected ({cross_border['matches_found']} instances):"
        )

        for item in cross_border["details"]:
            explanation_lines.append(
                f"- ₹{item['amount']:,} transferred to "
                f"{item['destination_country']} on "
                f"{format_datetime(item['timestamp'])}."
            )

    # ---------------- VELOCITY ----------------
    velocity = tool_results.get("detect_velocity_spike")
    if velocity and velocity["matches_found"] > 0:
        explanation_lines.append(
            "\nHigh transaction velocity detected within a short time window."
        )

    explanation_lines.append(
        f"\nFinal Recommendation: {investigation_result['recommendation']}."
    )

    return "\n".join(explanation_lines)