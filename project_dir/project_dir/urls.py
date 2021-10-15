from django.urls import path
from django_app.views import home, send_message, get_messages, handle_incoming_messages

urlpatterns = [
    path('', home),
    path('send', send_message),
    path('messages', get_messages),
    path('notify', handle_incoming_messages),
]
