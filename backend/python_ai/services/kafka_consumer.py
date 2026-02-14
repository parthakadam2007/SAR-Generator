from kafka import KafkaConsumer
import json
from routes.pipeline_route import pipeline_router

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

        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        key_deserializer=lambda k: k.decode("utf-8") if k else None
    )
    print(" 🚨created_consumer")

    return consumer


def process_alert(message):
    print("🚨 New Bank Alert Received",flush=True)

    temp_dict  = json.loads(message) 
    print("🚨"+ pipeline_router(temp_dict),flush=True)

    # TODO  save to DB, trigger pipeline, etc.


def start_consumer():
    print("⏳ Waiting for Kafka...")

    consumer = create_consumer()
    print("✅ Connected. Listening on topic:", TOPIC)
    
    for msg in consumer:
        process_alert(msg.value)