from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class MainConsumer(WebsocketConsumer):
    def connect(self, **kwargs):
        print("HII")
        self.room_name = "main_room"
        self.group_name = 'main_room'
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name,
        )
        self.accept()
        self.send(text_data = json.dumps({
            "message":"connection made"
        }))

    def receive(self, text_data=None, bytes_data=None):
        pass

    def disconnect(self, close_code):
        pass