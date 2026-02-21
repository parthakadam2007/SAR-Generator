import json
from aiokafka import AIOKafkaConsumer

# from backend.python_ai import routes
from services.riskscore_service import calculate_risk
from services.evidence_generator import generate_evidence
from routes.pipeline_route import RISK_EVIDENCE_THRESHOLD
from models.create_case_analysis import create_case_analysis
from routes.ai_route import sar_pipeline


KAFKA_BROKER = "kafka:9092"
TOPIC = "bankAlert"
GROUP_ID = "bank-alert-consumers"


async def start_consumer():

    consumer = AIOKafkaConsumer(
        TOPIC,
        bootstrap_servers=KAFKA_BROKER,
        group_id=GROUP_ID,
        auto_offset_reset="earliest",
        value_deserializer=lambda v: json.loads(v.decode())
    )

    await consumer.start()

    print("✅ Kafka Consumer Started")

    try:
        async for msg in consumer:

            try:
                await process_alert(msg.value)   # ✅ awaited

            except Exception as e:
                print("⚠️ Error processing message:", e, flush=True)

    finally:
        await consumer.stop()


async def process_alert(message):

    print("🚨 New Bank Alert Received", flush=True)

    # case = message if isinstance(message, dict) else json.loads(message)

    # risk_result = calculate_risk(case)

    # response = {
    #     "status": "success",
    #     "input": case,
    #     "risk": risk_result,
    #     "threshold": RISK_EVIDENCE_THRESHOLD,
    #     "evidence_generated": False,
    #     "evidence": []
    # }

    # if risk_result.get("risk_score", 0) >= RISK_EVIDENCE_THRESHOLD:
    #     response["evidence_generated"] = True
    #     response["evidence"] = generate_evidence(case, risk_result)

    sar_pipeline_response = await sar_pipeline(message)   # ✅ awaited
   
    try:
        print( sar_pipeline_response, flush=True)
        await create_case_analysis(sar_pipeline_response)   # ✅ awaited
        print("✅ Case saved")
            
    except Exception as e:
        print("⚠️ DB error:", e, flush=True)
        try:
            # Save SAR pipeline response to file
            with open("sar_pipeline_response.json", "w") as f:
                json.dump(sar_pipeline_response, f, indent=2)

                print("✅ SAR pipeline response saved to file", flush=True)
        except Exception as e:
            print("⚠️ Error saving SAR pipeline response to file:", e, flush=True)
