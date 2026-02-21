from config.database import get_driver

def insert_case_data(case_json: dict):

    driver = get_driver()

    with driver.session() as session:

        session.execute_write(_create_case_graph, case_json)

    return {"status": "success"}


def _create_case_graph(tx, data):

    # Create Case
    tx.run("""
        MERGE (c:Case {case_id: $case_id})
        SET c.generated_at = datetime($generated_at),
            c.institution = $institution
    """, 
    case_id=data["case_id"],
    generated_at=data["generated_at"],
    institution=data["institution"]
    )

    # Create Customer
    customer = data["customer_kyc"]

    tx.run("""
        MERGE (cust:Customer {customer_id: $customer_id})
        SET cust.full_name = $full_name,
            cust.risk_category = $risk_category,
            cust.occupation = $occupation
    """,
    customer_id=customer["customer_id"],
    full_name=customer["full_name"],
    risk_category=customer["risk_category"],
    occupation=customer["occupation"]
    )

    # Create Main Account
    account = data["account_profile"]

    tx.run("""
        MERGE (acc:Account {account_number: $account_number})
        SET acc.account_type = $account_type,
            acc.average_monthly_balance = $avg_balance
    """,
    account_number=account["account_number"],
    account_type=account["account_type"],
    avg_balance=account["average_monthly_balance"]
    )

    # Create Relationships
    tx.run("""
        MATCH (c:Case {case_id: $case_id})
        MATCH (cust:Customer {customer_id: $customer_id})
        MATCH (acc:Account {account_number: $account_number})

        MERGE (c)-[:INVOLVES_CUSTOMER]->(cust)
        MERGE (cust)-[:OWNS]->(acc)
        MERGE (c)-[:INVOLVES_ACCOUNT]->(acc)
    """,
    case_id=data["case_id"],
    customer_id=customer["customer_id"],
    account_number=account["account_number"]
    )

    # Insert Transactions
    for tx_data in data["transactions"]:
        tx.run("""
            MERGE (fromAcc:Account {account_number: $from_account})
            MERGE (toAcc:Account {account_number: $to_account})
            MERGE (fromAcc)-[:TRANSFERRED {
                tx_id: $tx_id,
                amount: $amount,
                timestamp: datetime($timestamp),
                country: $country
            }]->(toAcc)
        """,
        from_account=tx_data["from_account"],
        to_account=tx_data["to_account"],
        tx_id=tx_data["tx_id"],
        amount=tx_data["amount"],
        timestamp=tx_data["timestamp"],
        country=tx_data["country"]
        )

    for alert in data.get("alerts", []):
        tx.run("""
            MERGE (a:Alert {alert_id: $alert_id})
            SET a.type = $type,
                a.description = $description,
                a.severity = $severity,
                a.trigger_time = datetime($trigger_time)
        """,
        alert_id=alert["alert_id"],
        type=alert["type"],
        description=alert["description"],
        severity=alert["severity"],
        trigger_time=alert["trigger_time"]
        )

        tx.run("""
            MATCH (acc:Account {account_number: $account_number})
            MATCH (a:Alert {alert_id: $alert_id})
            MERGE (acc)-[:HAS_ALERT]->(a)
        """,
        account_number=data["account_profile"]["account_number"],
        alert_id=alert["alert_id"]
        )