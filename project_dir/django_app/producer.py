import json
import pika
from project_dir.settings import RABBITMQ_HOST, RABBITMQ_USER, RABBITMQ_PASS

credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST, heartbeat=600, blocked_connection_timeout=300, credentials=credentials))
channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='messages', body=json.dumps(body), properties=properties)
