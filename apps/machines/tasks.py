from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from django.core.exceptions import ObjectDoesNotExist

from .models import Machine

from .serializers import RealtimeSerializer

@shared_task
def get_machine_data(channel_group_name, machine_pk):
    try:
        machine = Machine.objects.filter(pk=machine_pk)[0]
        machine = machine.machineRealtimeData
    except ObjectDoesNotExist:
        machine = None  # Change to end websocket connection

    machine_data = RealtimeSerializer(machine)
    
    message = {
        'type': 'send_machine_data',
        'machine_data' : machine_data.data
        }
    channel_layer = get_channel_layer()
    
    async_to_sync(channel_layer.group_send)(channel_group_name, message)