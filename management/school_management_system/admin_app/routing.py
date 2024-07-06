# admin_app/routing.py
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/somepath/', consumers.SomeConsumer.as_asgi()),
]
