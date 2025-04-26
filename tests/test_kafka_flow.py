import pytest
from src.kafka_producer import send_fake_messages
from src.kafka_consumer import consume_messages

TOPIC = "finance-topic"  # Usando o tópico 'finance-topic' definido no producer

@pytest.fixture(scope="module")
def kafka_messages():
    """Fixture para gerar e consumir mensagens do Kafka."""
    send_fake_messages(TOPIC, num_messages=100)
    return consume_messages(TOPIC)

def test_messages_are_consumed(kafka_messages):
    """Teste para verificar se as mensagens foram consumidas."""
    assert len(kafka_messages) > 0, "Não foram consumidas mensagens."

def test_message_contains_required_fields(kafka_messages):
    """Teste para verificar se todas as mensagens possuem os campos esperados."""
    for message in kafka_messages:
        assert 'name' in message, f"Mensagem consumida não contém 'name': {message}"
        assert 'age' in message, f"Mensagem consumida não contém 'age': {message}"
        assert 'transaction_value' in message, f"Mensagem consumida não contém 'transaction_value': {message}"
        assert 'transaction_type' in message, f"Mensagem consumida não contém 'transaction_type': {message}"
        assert 'timestamp' in message, f"Mensagem consumida não contém 'timestamp': {message}"

def test_transaction_value_range(kafka_messages):
    """Teste para verificar se os valores de 'transaction_value' estão no intervalo esperado."""
    for message in kafka_messages:
        assert 0 < message['transaction_value'] < 10000, f"Valor da transação fora do intervalo esperado: {message['transaction_value']}"

def test_timestamps_are_ordered(kafka_messages):
    """Teste para verificar se os timestamps estão ordenados cronologicamente."""
    timestamps = [message['timestamp'] for message in kafka_messages]
    assert timestamps == sorted(timestamps), "Os timestamps das mensagens não estão ordenados cronologicamente."

def test_messages_are_from_same_day(kafka_messages):
    """Teste para verificar se todas as mensagens possuem timestamps do mesmo dia."""
    from datetime import datetime

    # Extrair apenas a data (ano, mês, dia) de cada timestamp
    dates = {datetime.fromisoformat(message['timestamp']).date() for message in kafka_messages}
    assert len(dates) == 1, f"As mensagens possuem timestamps de dias diferentes: {dates}"