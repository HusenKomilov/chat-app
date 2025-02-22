from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from chat import models


class ChatConsumer(WebsocketConsumer):

    def fetch_message(self, data):
        messages = models.Message.objects.all().order_by("created_ad")[:10]
        content = {
            "messages": self.messages_to_json(messages)
        }
        self.send_chat_message(content)

    def new_message(self, data):
        author = data["from"]
        author_user = models.Profile.objects.filter(username=author)[0]
        message = models.Message.objects.create(
            author = author_user,
            content = data["message"]
        )
        content = {
            "command": "new_message",
            "message": self.message_to_json
        }

        return self.send_chat_message(content)

    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    def message_to_json(self, message):
        return {
            "user": message.author.username,
            "message": message.message,
            "time": message.created_ad
        }
    commands = {
        "fetch_message": fetch_message,
        "new_message": new_message
    }

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = "chats_%s" % self.room_name
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_layer
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)

    def send_chat_message(self, message):
        message = text_data_json["message"]
        asyn_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message
            }
        )

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    def chat_message(self, event):
        message = event["message"]
        self.send(text_data=json.dumps(message))
