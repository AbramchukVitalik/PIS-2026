# services/notification_service/consumer.py
import pika
import json

def callback(ch, method, properties, body):
    event = json.loads(body)
    print("NOTIFICATION:", event)

connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost")
)
channel = connection.channel()

channel.exchange_declare(exchange="notes", exchange_type="fanout")

queue = channel.queue_declare(queue="", exclusive=True)
channel.queue_bind(exchange="notes", queue=queue.method.queue)

channel.basic_consume(
    queue=queue.method.queue,
    on_message_callback=callback,
    auto_ack=True
)

print("Notification service started")
channel.start_consuming()