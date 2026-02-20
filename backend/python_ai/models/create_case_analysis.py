import database as db
from datetime import datetime

async def create_case_analysis(data: dict):
    if db.pool is None:
      raise RuntimeError("DB pool not initialized. Call init_db() first.")

    async with db.pool.acquire() as conn:
        async with conn.transaction():

            # Insert case analysis
            analysis_id = await conn.fetchval(
                """
                INSERT INTO case_analysis
                (case_id, status, risk_score, classification, threshold, evidence_generated)
                VALUES ($1,$2,$3,$4,$5,$6)
                RETURNING id
                """,
                data["input"]["case_id"],
                data["status"],
                data["risk"]["risk_score"],
                data["risk"]["classification"],
                data["threshold"],
                data["evidence_generated"]
            )

            # Risk breakdown
            await conn.execute(
                """
                INSERT INTO risk_breakdown
                (analysis_id, customer_risk, alert_risk, geographic_risk,
                 pattern_risk, transaction_risk)
                VALUES ($1,$2,$3,$4,$5,$6)
                """,
                analysis_id,
                data["risk"]["breakdown"]["customer_risk"],
                data["risk"]["breakdown"]["alert_risk"],
                data["risk"]["breakdown"]["geographic_risk"],
                data["risk"]["breakdown"]["pattern_risk"],
                data["risk"]["breakdown"]["transaction_risk"]
            )

            # Evidence
            for ev in data["evidence"]:
                await conn.execute(
                    """
                    INSERT INTO evidence (analysis_id, evidence_type, description)
                    VALUES ($1,$2,$3)
                    """,
                    analysis_id,
                    "system",
                    ev,
                )
            print(f"SAR  generated for case_id {data['input']['case_id']}", flush=True)


            sar_id = None
            try:
                sar_id = await conn.fetchval(
                    """
                    INSERT INTO sar_reports
                    (case_id, analysis_id, sar_number, sar_summary,
                        narrative, transaction_analysis, recommended_action)
                    VALUES ($1,$2,$3,$4,$5,$6,$7)
                    RETURNING id
                    """,
                    data["input"]["case_id"],
                    analysis_id,
                    data["input"]["case_id"],  # TODO using case_id as sar_number for now
                    "summary for case_id ",  # TODO placeholder summary
                    "narrative for case_id ",  # TODO placeholder narrative
                    "transaction analysis for case_id ",  # TODO placeholder transaction analysis
                    "recommended action for case_id "  # TODO placeholder recommended action
                )
            except Exception as e:
                print(f"Error inserting SAR report for case_id {data['input']['case_id']}: {e}", flush=True)
                raise e

            print(f"SAR subject saving  for case_id {data['input']['case_id']}", flush=True)

            # Get SAR section safely
            sar = data.get("sar")

            if not sar:
                raise ValueError("SAR section is missing in input data")

            # Get subject profile safely
            subject = sar.get("subject_profile")

            if not subject:
                print(
                    f"Error: Subject profile is missing for case_id {data.get('input', {}).get('case_id')}",
                    flush=True
                )
                raise ValueError("Subject profile is required to save SAR report")

            try:
            # Subject
                # debug print values
                print(
                    "Debug sar_subject values:",
                    sar_id,
                    subject.get("customer_id"),
                    subject.get("full_name"),
                    subject.get("dob"),
                    subject.get("pan"),
                    subject.get("aadhaar_last4"),
                    subject.get("occupation"),
                    subject.get("declared_annual_income"),
                    data["sar"]["risk_assessment"]["risk_category"],
                    subject.get("address"),
                    subject.get("kyc_last_updated"),
                    flush=True
                )

                await conn.execute(
                    """
                    INSERT INTO sar_subjects
                    (sar_id, customer_id, full_name, dob, pan,
                        aadhaar_last4, occupation, declared_annual_income,
                        risk_category, address, kyc_last_updated)
                    VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11)
                    """,
                    sar_id,
                    subject["customer_id"],
                    subject["full_name"],
                    subject["dob"],
                    subject["pan"],
                    subject["aadhaar_last4"],
                    subject["occupation"],
                    subject["declared_annual_income"],
                    data["sar"]["risk_assessment"]["risk_category"],
                    subject["address"],
                    subject["kyc_last_updated"]
                )

            except Exception as e:
                print(f"Error inserting SAR subject for case_id {data['input']['case_id']} {sar['risk_assessment']['risk_category']}: {e}", flush=True)
                raise e



            print(f"SAR account saving  for case_id {data['input']['case_id']}", flush=True)

            # Accounts
            try:
                await conn.execute(
                    """
                    INSERT INTO sar_accounts
                    (sar_id, account_number, account_type, opened_date,
                        average_monthly_balance, average_monthly_credit,
                        average_monthly_debit, usual_transaction_pattern)
                    VALUES ($1,$2,$3,$4,$5,$6,$7,$8)
                    """,
                    sar_id,
                    subject["account_number"],
                    subject["account_type"],
                    subject["opened_date"],
                    subject["average_monthly_balance"],
                    subject["average_monthly_credit"],
                    subject["average_monthly_debit"],
                    subject["usual_transaction_pattern"]
                )
            except Exception as e:
                print(f"Error inserting SAR account for case_id {data['input']['case_id']}: {e}", flush=True)
                raise e

            print(f"SAR sar_risk_assessments saving  for case_id {data['input']['case_id']}", flush=True)


            risk = sar.get("risk_assessment")
            if not risk:
                print(
                    f"Error: Risk assessment is missing for case_id {data.get('input', {}).get('case_id')}",
                    flush=True
                )
                raise ValueError("Risk assessment is required to save SAR report")
            
            # Risk assessment
            try:
                alerts_str = ", ".join(risk.get("alerts_triggered", []))
                inconsistencies_str = ", ".join(risk.get("inconsistencies", []))
                
                await conn.execute(
                    """
                    INSERT INTO sar_risk_assessments
                    (sar_id, risk_category, alerts_triggered, inconsistencies)
                    VALUES ($1,$2,$3,$4)
                    """,
                    sar_id,
                    risk.get("risk_category"),
                    alerts_str,
                    inconsistencies_str
                )
            except Exception as e:
                print(f"Error inserting SAR risk assessment for case_id {data['input']['case_id']}: {e}", flush=True)
                raise e

            print(f"SAR suspicious_indicators saving  for case_id {data['input']['case_id']}", flush=True)

            # Indicators
            try:
                for ind in data["sar"]["suspicious_indicators"]:
                    await conn.execute(
                        """
                        INSERT INTO sar_indicators
                        (sar_id, indicator_text)
                        VALUES ($1,$2)
                        """,
                        sar_id,
                        ind,
                    )
            except Exception as e:
                print(f"Error inserting SAR indicators for case_id {data['input']['case_id']}: {e}", flush=True)
                raise e
            print(f"SAR report saved with id {sar_id} for case_id {data['input']['case_id']}", flush=True)