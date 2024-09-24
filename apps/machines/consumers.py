import json
import uuid

from channels.generic.websocket import AsyncWebsocketConsumer

from celery.result import AsyncResult

from .tasks import get_machine_data

class MachineRealtimeDataConsumer(AsyncWebsocketConsumer):

    task_id = None
        
    async def connect(self):
        #Check that machine pk is an int
        self.machine_pk = self.scope['url_route']['kwargs']['machine_pk']
        
        #Create group name with uuid
        self.channel_group_name = f'{uuid.uuid4().hex}'
        
        await self.channel_layer.group_add(
            self.channel_group_name,
            self.channel_name
        )

        await self.accept()

        task = get_machine_data.apply_async(args=[self.channel_group_name, self.machine_pk], countdown=2)
        
        self.task_id = task.id
        
    async def disconnect(self, close_code):
        if self.task_id:
            task_result = AsyncResult(self.task_id)
            if not task_result.ready():  # Check if the task is still running
                task_result.revoke(terminate=True)  # Terminate the task
            self.task_id = None  # Clear the task ID
            
        await self.channel_layer.group_discard(
            self.channel_group_name,
            self.channel_name
        )
    
    async def receive(self, text_data=None):
        print(f'Message received: {text_data}')
        pass
    
    async def send_machine_data(self, event):
        machine_data = event['machine_data']
        await self.send(text_data=json.dumps({
            'machine_data' : machine_data
        }))
        task = get_machine_data.apply_async(args=[self.channel_group_name, self.machine_pk], countdown=2)
        
        self.task_id = task.id