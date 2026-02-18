from python_ai.database import pool

async def creaate_case_analysis(data:dict):
    """
    Create a new case analysis in the database.
    """
    async with pool.acquire() as conn:
        async with conn.transaction():

            # Insert case_analysis
            analysis_id = await conn.fetchval(
                """
                INSERT INTO case_analysis
                (case_id, status, risk_score, classification, threshold, evidence_generated)
                VALUES ($1, $2, $3, $4, $5, $6)
                RETURNING id
                """,
                data["input"]["case_id"],
                data["status"],
                data["risk"]["risk_score"],
                data["risk"]["classification"],
                data["threshold"],
                data["evidence_generated"]
            )

            await conn.execute(
                "INSERT INTO risk_breakdown (analysis_id, customer_risk,alert_risk,pattern_risk,transaction_risk) VALUES ($1, $2, $3, $4, $5)",
                analysis_id,
                data["risk"]["breakdown"]["customer_risk"],
                data["risk"]["breakdown"]["alert_risk"],
                data["risk"]["breakdown"]["pattern_risk"],
                data["risk"]["breakdown"]["transaction_risk"]
            )


            # Insert evidence
            for ev in data["evidence"]:
                await conn.execute(
                    """
                    INSERT INTO evidence (analysis_id, type, description, details)
                    VALUES ($1, $2, $3, $4)
                    """,
                    analysis_id,
                    "demo_type",
                    ev,
                    "demo_details"
                    )

            # Insert in sar
            if data["sar_generated"]:
                await conn.execute(
                    """
                    INSERT INTO sar (case_id, analysis_id, status)
                    VALUES ($1, $2, $3)
                    """,
                    data["input"]["case_id"],
                    analysis_id,
                    "generated"
                )