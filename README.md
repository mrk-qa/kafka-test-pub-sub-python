# Messaging POC

POC de testes automatizados em filas de mensageria usando Kafka + Python.

## Como rodar:

1. Subir o Kafka com Docker:
    ```bash
    docker-compose up -d
    ```

2. Instalar dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. Rodar os testes:
    ```bash
    pytest
    ```
