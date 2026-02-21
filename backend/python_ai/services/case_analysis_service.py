from config.database import get_driver
from statistics import mean
from datetime import datetime


def analyze_case(case_id: str):

    driver = get_driver()

   
    query = """
   MATCH (c:Case {case_id: $case_id})
    OPTIONAL MATCH (c)-[:INVOLVES_CUSTOMER]->(cust:Customer)
    OPTIONAL MATCH (cust)-[:OWNS]->(mainAcc:Account)

    OPTIONAL MATCH (mainAcc)<-[t1:TRANSFERRED]-(a1:Account)
    OPTIONAL MATCH (mainAcc)-[t2:TRANSFERRED]->(a2:Account)

    OPTIONAL MATCH (a2)-[t3:TRANSFERRED]->(a3:Account)

    OPTIONAL MATCH (mainAcc)-[:HAS_ALERT]->(alert:Alert)

    RETURN
    collect(DISTINCT cust) AS customers,
    collect(DISTINCT mainAcc) AS accounts,
    collect(DISTINCT t1) +
    collect(DISTINCT t2) +
    collect(DISTINCT t3) AS transfers,
    collect(DISTINCT alert) AS alerts
    """


    with driver.session() as session:
        record = session.run(query, case_id=case_id).single()

        if not record:
            return None

        
        transactions = [
            {**t._properties} for t in record["transfers"] if t
        ]
        accounts = [{**a._properties} for a in record["accounts"] if a]
        alerts = [dict(a) for a in record["alerts"] if a]

    # -----------------------------
    # RULE ENGINE STARTS HERE
    # -----------------------------

    triggered_rules = []
    risk_score = 0

    # 🔴 Rule 1: High Value Transaction
    high_value = [t for t in transactions if t.get("amount", 0) > 200000]
    if high_value:
        triggered_rules.append("High Value Transactions > 200K")
        risk_score += 20

    # 🔴 Rule 2: Structuring (many small txns under 10K)
    small_txns = [t for t in transactions if 9000 <= t.get("amount", 0) <= 10000]
    if len(small_txns) >= 5:
        triggered_rules.append("Possible Structuring Detected")
        risk_score += 25

    # 🔴 Rule 3: Velocity Spike (many txns same day)
    date_count = {}
    for t in transactions:
        date = t.get("timestamp")
        if date:
            date_count[date] = date_count.get(date, 0) + 1

    if any(v > 10 for v in date_count.values()):
        triggered_rules.append("High Transaction Velocity")
        risk_score += 15

    # 🔴 Rule 4: Dormant Account Reactivation
    if transactions:
        dates = sorted([
            datetime.fromisoformat(str(t["timestamp"]))
            for t in transactions if "date" in t
        ])
        if len(dates) >= 2:
            gap = (dates[-1] - dates[0]).days
            if gap > 180:
                triggered_rules.append("Dormant Account Reactivation")
                risk_score += 10

    # 🔴 Rule 5: Multiple Accounts
    if len(accounts) > 3:
        triggered_rules.append("Multiple Account Usage")
        risk_score += 15

    # 🔴 Rule 6: Alert Correlation
    if len(alerts) > 0:
        triggered_rules.append("System Alerts Present")
        risk_score += 20

    # 🔴 Rule 7: Rapid Fund Movement (Layering)
    if len(transactions) > 15:
        avg_amt = mean([t.get("amount", 0) for t in transactions])
        if avg_amt > 100000:
            triggered_rules.append("Possible Layering Activity")
            risk_score += 20
    # 🔴 Rule 8: Rapid Fund Chain Movement
    if len(transactions) >= 3:
        times = sorted([
            datetime.fromisoformat(str(t["timestamp"]))
            for t in transactions if "timestamp" in t
        ])
        if times and (times[-1] - times[0]).total_seconds() < 3600:
            triggered_rules.append("Rapid Sequential Fund Movement (Layering)")
            risk_score += 30

        # 🔴 Rule 9: Cross Border Movement
    if any(t.get("country") and t.get("country") != "India" for t in transactions):
        triggered_rules.append("Cross Border Transfer Detected")
        risk_score += 25
    # 🔴 Rule 10: Pass-Through Account Behavior
    amounts = [t.get("amount", 0) for t in transactions]
    if len(amounts) >= 2:
        if len(set(amounts)) == 1:
            triggered_rules.append("Pass-Through Account (Amount Mirroring)")
            risk_score += 25

    # 🔴 Rule 11: Amount Disproportionate to Account Profile
    if accounts:
        avg_credit = accounts[0].get("average_monthly_credit", 0)
        for t in transactions:
            if avg_credit and t.get("amount", 0) > (avg_credit * 2):
                triggered_rules.append("Transaction Disproportionate to Account Profile")
                risk_score += 20
                break

    # 🔴 Rule 12: Multiple Intermediary Accounts
    unique_destinations = set()
    for t in transactions:
        unique_destinations.add(t.get("tx_id"))

    if len(transactions) >= 3:
        triggered_rules.append("Multiple Intermediary Routing Detected")
        risk_score += 20
    # -----------------------------
    # Network Risk (Graph Based)
    # -----------------------------

    network_query = """
    MATCH (c:Case {case_id: $case_id})-[:INVOLVES_CUSTOMER]->(cust)
    MATCH (cust)-[:OWNS]->(acc)
    MATCH (acc)-[t:TRANSFERRED]->()
    RETURN count(DISTINCT t) AS txn_count

    """

    with driver.session() as session:
        net_record = session.run(network_query, case_id=case_id).single()
        txn_count = net_record["txn_count"] if net_record else 0

    if txn_count > 50:
        triggered_rules.append("Large Transaction Network")
        risk_score += 20

    # -----------------------------
    # Risk Level Classification
    # -----------------------------

    if risk_score >= 70:
        risk_level = "HIGH"
        recommendation = "STR strongly recommended"
    elif risk_score >= 40:
        risk_level = "MEDIUM"
        recommendation = "Manual review required"
    else:
        risk_level = "LOW"
        recommendation = "Monitor"

    
    driver.close()

    return {
        "case_id": case_id,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "triggered_rules": triggered_rules,
        "transaction_count": len(transactions),
        "account_count": len(accounts),
        "alert_count": len(alerts),
        "recommendation": recommendation
    }