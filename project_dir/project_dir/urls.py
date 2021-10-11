from django.urls import path
from django_app.views import home, send_message, get_messages

urlpatterns = [
    path('', home),
    path('send', send_message),
    path('messages', get_messages),
]
