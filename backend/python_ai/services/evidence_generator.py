from datetime import datetime
from collections import defaultdict

# -------------------------------------------------------
# Helper Functions
# -------------------------------------------------------

def format_inr(amount):
    """Format number into Indian currency format with ₹ symbol."""
    amount = float(amount)
    negative = amount < 0
    amount = abs(int(round(amount)))
    s = str(amount)
    if len(s) <= 3:
        result = s
    else:
        result = s[-3:]
        s = s[:-3]
        while len(s) > 2:
            result = s[-2:] + "," + result
            s = s[:-2]
        if s:
            result = s + "," + result
    return f"{'-' if negative else ''}₹{result}"


def parse_timestamp(ts):
    """Parse ISO timestamp safely."""
    try:
        return datetime.fromisoformat(ts)
    except Exception:
        return None


# -------------------------------------------------------
# Deterministic Evidence Generator
# -------------------------------------------------------

def generate_evidence(case_json, risk_result):
    """
    Generate deterministic, factual, regulator-safe evidence statements.
    No inference. No AI. No assumptions.
    """

    evidence = []

    customer = case_json["customer_kyc"]
    account = case_json["account_profile"]
    alerts = case_json["alerts"]
    transactions = case_json["transactions"]
    breakdown = risk_result["breakdown"]

    # =====================================================
    # A) Customer Risk Evidence
    # =====================================================

    evidence.append(f"Customer KYC risk category is {customer['risk_category']}.")
    evidence.append(f"Declared annual income is {format_inr(customer['declared_annual_income'])}.")
    evidence.append(f"Customer occupation is {customer.get('occupation', 'Not Provided')}.")

    # =====================================================
    # B) Alert Risk Evidence
    # =====================================================
    for alert in alerts:
        trigger_time = alert.get("trigger_time", "Unknown Time")
        evidence.append(
            f"Alert '{alert.get('type')}' with severity "
            f"'{alert.get('severity')}' triggered at {trigger_time}."
        )


    # =====================================================
    # C) Geographic Risk Evidence
    # =====================================================

    foreign_txs = [tx for tx in transactions if tx["country"] != "India"]
    foreign_count = len(foreign_txs)

    if foreign_count > 0:
        countries = sorted(set(tx["country"] for tx in foreign_txs))
        evidence.append(f"{foreign_count} foreign transaction(s) detected.")
        evidence.append(f"Foreign country(ies) involved: {', '.join(countries)}.")
        evidence.append("Funds were transferred outside India.")
    else:
        evidence.append("No foreign transactions detected.")

    # =====================================================
    # D) Circular Pattern Risk Evidence
    # =====================================================

    if breakdown.get("pattern_risk", 0) > 0:
        evidence.append("Circular fund flow pattern detected among accounts.")

    # =====================================================
    # E) Transaction Anomaly Evidence
    # =====================================================

    total_volume = sum(tx["amount"] for tx in transactions)
    income = customer["declared_annual_income"]
    avg_credit = account["average_monthly_credit"]

    evidence.append(f"Total transaction volume is {format_inr(total_volume)}.")
    evidence.append(f"Average monthly credit is {format_inr(avg_credit)}.")

    income_ratio = total_volume / max(income, 1)
    credit_ratio = total_volume / max(avg_credit * 12, 1)

    if income_ratio > 1:
        evidence.append("Total transaction volume exceeds declared annual income.")

    elif income_ratio > 2:
        evidence.append("Total transaction volume is more than twice the declared annual income.")

    if credit_ratio > 1:
        evidence.append("Total transaction volume exceeds expected annual credit based on account profile.")

    # =====================================================
    # F) Velocity Pattern Evidence
    # =====================================================

    parsed_txs = []
    for tx in transactions:
        dt = parse_timestamp(tx["timestamp"])
        if dt:
            parsed_txs.append((dt, tx))

    parsed_txs.sort(key=lambda x: x[0])

    # Multiple transactions within 1 hour window
    for i in range(len(parsed_txs)):
        base_time = parsed_txs[i][0]
        count = 1
        for j in range(i + 1, len(parsed_txs)):
            if (parsed_txs[j][0] - base_time).total_seconds() <= 3600:
                count += 1
            else:
                break
        if count >= 3:
            evidence.append(f"{count} transactions occurred within a one-hour window starting at {base_time.isoformat()}.")
            break

    # Same-day large inflow + outflow
    daily_flows = defaultdict(lambda: {"in": 0, "out": 0})

    for dt, tx in parsed_txs:
        date_key = dt.date()
        if tx["to_account"] == account["account_number"]:
            daily_flows[date_key]["in"] += tx["amount"]
        if tx["from_account"] == account["account_number"]:
            daily_flows[date_key]["out"] += tx["amount"]

    for date, flows in daily_flows.items():
        if flows["in"] > 0 and flows["out"] > 0:
            evidence.append(
                f"On {date.isoformat()}, same-day inflow of {format_inr(flows['in'])} and outflow of {format_inr(flows['out'])} detected."
            )

    return evidence