# services/request_service/infrastructure/rabbitmq_publisher.py
import json
import pika

class RabbitPublisher:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters("localhost")
        )
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange="notes", exchange_type="fanout")

    def publish(self, event: dict):
        self.channel.basic_publish(
            exchange="notes",
            routing_key="",
            body=json.dumps(event)
        )