import time
from kafka import KafkaConsumer
import json
from services.riskscore_service import calculate_risk
from services.evidence_generator import generate_evidence
from routes.pipeline_route import RISK_EVIDENCE_THRESHOLD

KAFKA_BROKER = "kafka:9092"
TOPIC = "bankAlert"
GROUP_ID = "bank-alert-consumers"


def create_consumer():

    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers=KAFKA_BROKER,
        group_id=GROUP_ID,

        auto_offset_reset="earliest",   # read from start if new group
        enable_auto_commit=True,

        # value_deserializer returns a dict for JSON payloads
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        key_deserializer=lambda k: k.decode("utf-8") if k else None
    )
    print(" 🚨created_consumer")

    return consumer


def process_alert(message):
    """Process a Kafka alert message.

    Accepts either a dict (already-deserialized) or a JSON string.
    Runs the same risk/evidence pipeline used by the API routes.
    """
    print("🚨 New Bank Alert Received", flush=True)
    print(message)

    # message should already be a dict because of value_deserializer
    if isinstance(message, dict):
        case = message
    else:
        try:
            case = json.loads(message)
        except Exception as e:
            print("⚠️ Failed to parse Kafka message:", e, flush=True)
            return

    # Reuse service-layer logic (synchronous)
    risk_result = calculate_risk(case)

    response = {
        "status": "success",
        "input": case,
        "risk": risk_result,
        "threshold": RISK_EVIDENCE_THRESHOLD,
        "evidence_generated": False,
        "evidence": []
    }

    if risk_result.get("risk_score", 0) >= RISK_EVIDENCE_THRESHOLD:
        response["evidence_generated"] = True
        response["evidence"] = generate_evidence(case, risk_result)

    print("🚨 Pipeline result:", json.dumps(response), flush=True)

    # TODO: persist to DB / emit to another topic / notify downstream


def start_consumer():
    print("⏳ Waiting for Kafka...")

    consumer = create_consumer()

    for msg in consumer:
        try:
            process_alert(msg.value)
        except Exception as e:
            # prevent the consumer thread from dying on unexpected errors
            print("⚠️ Error processing message:", e, flush=True)