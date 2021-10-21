import os
import json
import pika
import django
import pathlib
from sys import path

settings_file_path = f'{pathlib.Path(__file__).parent.resolve()}/project_dir/settings.py'
path.append(settings_file_path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_dir.settings') 
django.setup()
from django_app.models import Message
from project_dir.settings import CURRENT_SERVER_NAME, RABBITMQ_HOST

connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, heartbeat=600, blocked_connection_timeout=300))
channel = connection.channel()
channel.queue_declare(queue='ms2_messages')

def callback(ch, method, properties, body):
    print("Received in messages...", method, properties.content_type)
    print(body)
    data = json.loads(body)
    print(data)

    if properties.content_type == 'new_message':
        Message.objects.create(receiver=CURRENT_SERVER_NAME, sender=data['from'], message=data['message'])
        print("new_message received")

channel.basic_consume(queue='ms2_messages', on_message_callback=callback, auto_ack=True)
print("Started Consuming...")
channel.start_consuming()
