from collections import defaultdict

ALERT_WEIGHTS = {
    "Low": 5,
    "Medium": 10,
    "High": 18,
    "Critical": 25
}

MAX_COMPONENT = 25  # each dimension capped


def cap(value):
    return min(value, MAX_COMPONENT)


def calculate_risk(case_json):

    score = 0
    breakdown = {}

    # -------------------------
    # 1. Customer risk
    # -------------------------
    customer_risk_map = {
        "Low": 5,
        "Medium": 12,
        "High": 20
    }

    customer_risk = customer_risk_map.get(
        case_json["customer_kyc"]["risk_category"], 8
    )

    customer_risk = cap(customer_risk)
    score += customer_risk
    breakdown["customer_risk"] = customer_risk

    # -------------------------
    # 2. Alert risk (saturating)
    # -------------------------
    alert_score = sum(
        ALERT_WEIGHTS.get(alert["severity"], 0)
        for alert in case_json["alerts"]
    )

    alert_score = cap(alert_score)
    score += alert_score
    breakdown["alert_risk"] = alert_score

    # -------------------------
    # 3. Geographic risk
    # -------------------------
    foreign_count = sum(
        1 for tx in case_json["transactions"]
        if tx["country"] != "India"
    )

    geo_score = cap(foreign_count * 8)
    score += geo_score
    breakdown["geographic_risk"] = geo_score

    # -------------------------
    # 4. Circular pattern risk
    # -------------------------
    graph = defaultdict(list)

    for tx in case_json["transactions"]:
        graph[tx["from_account"]].append(tx["to_account"])

    visited = set()
    cycle_detected = False

    def dfs(node, stack):
        nonlocal cycle_detected
        if node in stack:
            cycle_detected = True
            return
        if node in visited:
            return

        visited.add(node)
        stack.add(node)

        for neighbor in graph.get(node, []):
            dfs(neighbor, stack)

        stack.remove(node)

    for node in list(graph.keys()):
        dfs(node, set())

    pattern_score = 20 if cycle_detected else 0
    pattern_score = cap(pattern_score)

    score += pattern_score
    breakdown["pattern_risk"] = pattern_score

    # -------------------------
    # 5. Transaction anomaly risk
    # -------------------------
    total_volume = sum(tx["amount"] for tx in case_json["transactions"])

    income = case_json["customer_kyc"]["declared_annual_income"]
    avg_credit = case_json["account_profile"]["average_monthly_credit"]

    # normalize ratios
    income_ratio = total_volume / max(income, 1)
    credit_ratio = total_volume / max(avg_credit * 12, 1)

    anomaly_score = 0

    if income_ratio > 1:
        anomaly_score += 12
    if income_ratio > 2:
        anomaly_score += 8
    if credit_ratio > 1:
        anomaly_score += 5

    anomaly_score = cap(anomaly_score)

    score += anomaly_score
    breakdown["transaction_risk"] = anomaly_score

    # -------------------------
    # Final classification
    # -------------------------
    if score < 25:
        classification = "Low"
    elif score < 50:
        classification = "Medium"
    elif score < 75:
        classification = "High"
    else:
        classification = "Critical"

    return {
        "risk_score": score,
        "classification": classification,
        "breakdown": breakdown
    }
