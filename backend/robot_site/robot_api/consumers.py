import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ApiConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Join room group
        print("WebSocket is connected.")
        await self.accept()

    def disconnect(self, close_code):
        # Leave room group
        pass

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))

    @staticmethod
    def ws_add(a: float, b: float) -> float:
        return a + b
