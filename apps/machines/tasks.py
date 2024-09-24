from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers

from .models import Machine

@shared_task
def get_machine_data(channel_group_name, machine_pk):
    try:
        machine = Machine.objects.filter(pk=machine_pk)
    except ObjectDoesNotExist:
        machine = None  # Change to end websocket connection
    print(machine)
    machine_json = serializers.serialize('json', machine)
    
    message = {
        'type': 'send_machine_data',
        'machine_data' : machine_json
        }
    channel_layer = get_channel_layer()
    
    async_to_sync(channel_layer.group_send)(channel_group_name, message)