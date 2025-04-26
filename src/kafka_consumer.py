from kafka import KafkaConsumer
import json
import os

BROKER = os.getenv("KAFKA_BROKER", "127.0.0.1:29092")

def consume_messages(topic, timeout_ms=5000):
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=[BROKER],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        consumer_timeout_ms=timeout_ms
    )

    messages = []
    for message in consumer:
        messages.append(message.value)

        print(f"MENSAGEM CONSUMIDA COM SUCESSO: {message.value} DO TOPICO: {message.topic}")

    consumer.close()
    return messages
