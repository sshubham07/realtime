from channels.generic.websocket import WebsocketConsumer

class MainConsumer(WebsocketConsumer):
    def connect(self, **kwargs):
        pass

    def recieve(self, text_data=None, bytes_data=None):
        pass

    def disconnect(self, close_code):
        pass