import pytest
from src.kafka_producer import send_fake_messages
from src.kafka_consumer import consume_messages

TOPIC = "finance-topic"  # Usando o tópico 'finance-topic' definido no producer

def test_kafka_flow():
    # Enviar 10 mensagens aleatórias para o Kafka (pode ajustar o número de mensagens conforme necessário)
    send_fake_messages(TOPIC, num_messages=100)

    # Consumir as mensagens do tópico
    messages = consume_messages(TOPIC)

    assert len(messages) > 0, f"Não foram consumidas mensagens. Mensagens consumidas: {messages}"
    assert 'transaction_value' in messages[0], f"Mensagem consumida não contém 'transaction_value'."
    
    # Exemplo de verificação de valores - podemos testar se um dos valores gerados está dentro de um intervalo aceitável
    assert 0 < messages[0]['transaction_value'] < 10000, f"Valor da transação fora do intervalo esperado: {messages[0]['transaction_value']}"
