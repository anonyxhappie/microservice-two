import requests
from django.http import HttpResponse
from .models import Message
from project_dir.settings import CURRENT_SERVER_NAME, OTHER_SERVERS, BASE_URL_MAPPING

def home(request):
    return HttpResponse(f'''
        <h1>Microservice <i>{CURRENT_SERVER_NAME}</i></h1>
        <p><b>Server Name:</b> {request.META['SERVER_NAME']}</p>
        <p><b>Server Port:</b> {request.META['SERVER_PORT']}</p>
        
        <p><b>Get Messages:</b> /messages</p>
        <p><b>Send Message:</b> /send?to=ms2&message=hello server, how are you?</p>
        
        <p><b>Other Available Servers:</b> {OTHER_SERVERS}</p> 
        ''')

def send_message(request):
    try:
        message = request.GET['message']
        to = request.GET['to']
    except KeyError as e:
        return HttpResponse(f"<div>Queryparam {str(e)} is required</div>")
    if to not in OTHER_SERVERS:
        return HttpResponse(f"Undefined server {to}")
 
    Message.objects.create(receiver=to, sender=CURRENT_SERVER_NAME, message=message)
    
    url = f'{BASE_URL_MAPPING[to]}/notify?from={CURRENT_SERVER_NAME}&message={message}'
    response = requests.get(url)
    if response.status_code != 200:
        return HttpResponse(f"<h1>Failed to send message to: {to}</h1>")

    return HttpResponse(f"<h1>Message sent to: {to}</h1>")

def handle_incoming_messages(request):
    try:
        message = request.GET['message']
        sender = request.GET['from']
    except KeyError as e:
        return HttpResponse(f"<div>Queryparam {str(e)} is required</div>")
    if sender not in OTHER_SERVERS:
        return HttpResponse(f"Undefined server {sender}")
 
    Message.objects.create(receiver=CURRENT_SERVER_NAME, sender=sender, message=message)
    return HttpResponse(f"<h1>Message ({message}) received from: {sender}</h1>")


def get_messages(_):
    messages = Message.objects.filter().order_by('-created_at')
    container = '<h1>Messages:</h1><div>'
    for m in messages:
        container += f'''
            <p>{m.sender} -> {m.receiver} : <b>{m.message}</b> ({m.created_at})</p>
        '''
    container += '</div>'
    return HttpResponse(container)
