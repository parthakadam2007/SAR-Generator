# ai_graph_tools.py

from config.database import get_driver
from datetime import datetime
from statistics import mean

# --------------------------------------------------
# BASE SAFE EXECUTOR
# --------------------------------------------------

def execute_read_query(query: str, params: dict):
    driver = get_driver()

    try:
        with driver.session() as session:
            result = session.run(query, **params)
            return [record.data() for record in result]
    finally:
        driver.close()


# --------------------------------------------------
# TOOL 1 — Layering Detection (Multi-hop)
# --------------------------------------------------

def detect_layering(case_id: str):

    query = """
    MATCH (c:Case {case_id: $case_id})
    MATCH (c)-[:INVOLVES_CUSTOMER]->(:Customer)-[:OWNS]->(main:Account)

    MATCH path = (main)-[:TRANSFERRED*2..4]->(dest:Account)

    WITH main.account_number AS source,
        dest.account_number AS destination,
        length(path) AS hop_count,
        reduce(total = 0, r IN relationships(path) | total + r.amount) AS total_amount

    WHERE total_amount > 500000

    RETURN source,
        destination,
        max(hop_count) AS hop_count,
        sum(total_amount) AS total_amount
    ORDER BY total_amount DESC
    """

    results = execute_read_query(query, {"case_id": case_id})

    return {
        "tool": "detect_layering",
        "case_id": case_id,
        "matches_found": len(results),
        "details": results
    }


# --------------------------------------------------
# TOOL 2 — Pass-Through Account Detection
# --------------------------------------------------

def detect_pass_through(case_id: str):

    query = """
    MATCH (c:Case {case_id: $case_id})
    MATCH (c)-[:INVOLVES_CUSTOMER]->(:Customer)-[:OWNS]->(acc:Account)

    MATCH (acc)<-[in:TRANSFERRED]-(src)
    MATCH (acc)-[out:TRANSFERRED]->(dest)

    WHERE in.amount = out.amount
    AND src <> dest
    AND abs(duration.between(in.timestamp, out.timestamp).minutes) <= 30

    WITH acc.account_number AS account,
        in.amount AS mirrored_amount,
        in.timestamp AS incoming_time,
        out.timestamp AS outgoing_time

    RETURN DISTINCT account,
        mirrored_amount,
        incoming_time,
        outgoing_time
    ORDER BY incoming_time
    """

    results = execute_read_query(query, {"case_id": case_id})

    return {
        "tool": "detect_pass_through",
        "case_id": case_id,
        "matches_found": len(results),
        "details": results
    }


# --------------------------------------------------
# TOOL 3 — Cross Border Detection
# --------------------------------------------------

def detect_cross_border(case_id: str):

    query = """
    MATCH (c:Case {case_id: $case_id})
    MATCH (c)-[:INVOLVES_CUSTOMER]->(:Customer)-[:OWNS]->(acc:Account)

    MATCH (acc)-[t:TRANSFERRED]->()

    WHERE t.country <> "India"
    AND t.amount > 200000

    RETURN acc.account_number AS account,
        t.amount AS amount,
        t.country AS destination_country,
        t.timestamp AS timestamp
    ORDER BY t.amount DESC
    """

    results = execute_read_query(query, {"case_id": case_id})

    return {
        "tool": "detect_cross_border",
        "case_id": case_id,
        "matches_found": len(results),
        "details": results
    }


# --------------------------------------------------
# TOOL 4 — Velocity Spike Detection
# --------------------------------------------------

def detect_velocity_spike(case_id: str):

    query = """
    MATCH (c:Case {case_id: $case_id})
    MATCH (c)-[:INVOLVES_CUSTOMER]->(:Customer)-[:OWNS]->(acc:Account)

    MATCH (acc)-[t:TRANSFERRED]->()

    WITH acc.account_number AS account,
        date(t.timestamp) AS tx_date,
        count(t) AS daily_count,
        sum(t.amount) AS daily_total

    WHERE daily_count >= 8 OR daily_total > 1000000

    RETURN account,
        tx_date,
        daily_count,
        daily_total
    ORDER BY daily_total DESC
    """

    results = execute_read_query(query, {"case_id": case_id})

    return {
        "tool": "detect_velocity_spike",
        "case_id": case_id,
        "matches_found": len(results),
        "details": results
    }


# --------------------------------------------------
# TOOL REGISTRY
# --------------------------------------------------

AML_TOOLS = {
    "detect_layering": detect_layering,
    "detect_pass_through": detect_pass_through,
    "detect_cross_border": detect_cross_border,
    "detect_velocity_spike": detect_velocity_spike
}