from kafka import KafkaProducer
from faker import Faker
from datetime import datetime
import json
import os
import pytz

BROKER = os.getenv("KAFKA_BROKER", "127.0.0.1:29092")
fake = Faker()
br_timezone = pytz.timezone('America/Sao_Paulo')

producer = KafkaProducer(
    bootstrap_servers=[BROKER],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_fake_message():
    timestamp = datetime.now(br_timezone).isoformat()
    
    return {
        "name": fake.name(),
        "age": fake.random_int(min=18, max=99),
        "transaction_value": round(fake.random_number(digits=4), 2),
        "transaction_type": fake.random_element(elements=("purchase", "withdrawal", "deposit")),
        "timestamp": timestamp
    }

def send_fake_messages(topic, num_messages):
    for _ in range(num_messages):
        message = generate_fake_message()
        print(f"ENVIANDO MENSAGEM PARA O TÓPICO: {topic} - MENSAGEM: {message}")
        producer.send(topic, message)
