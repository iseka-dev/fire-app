from channels.generic.websocket import AsyncWebSocketConsumer


class NewActiveFire(AsyncWebSocketConsumer):

    async def connect(self):

        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, fire):
        pass
