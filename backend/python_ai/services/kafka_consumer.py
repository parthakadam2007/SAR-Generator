from kafka import KafkaConsumer
import json
import time

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

    return consumer


def process_alert(message):
    # pipline(message)

    # JSON string
    print("🚨 New Bank Alert Received",flush=True)
    print(message)

def start_consumer():
    print("⏳ Waiting for Kafka...")

    consumer = create_consumer()

    for msg in consumer:
        process_alert(msg.value)