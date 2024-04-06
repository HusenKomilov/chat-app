from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
]
