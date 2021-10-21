import json
import pika
from project_dir.settings import RABBITMQ_HOST, RABBITMQ_USER, RABBITMQ_PASS
print('RABBITMQ_HOST', RABBITMQ_HOST)
# credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
# connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST, heartbeat=600, blocked_connection_timeout=300, credentials=credentials))
connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, heartbeat=600, blocked_connection_timeout=300))
channel = connection.channel()

def publish(method, queue, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key=queue, body=json.dumps(body), properties=properties)
