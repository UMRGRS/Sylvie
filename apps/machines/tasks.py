from celery import shared_task

from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers

from asgiref.sync import async_to_sync

from channels.layers import get_channel_layer

from .models import Machine

import logging
logger = logging.getLogger(__name__)

@shared_task
def getMachineData(group_name, machine_pk):
    logger.debug("Starting the task")
    try:
        machine = Machine.objects.get(pk=machine_pk)
    except ObjectDoesNotExist:
        machine = None  # Change to end websocket connection
    
    machine_json = serializers.serialize('json', machine)
    
    message = {
        'type': 'send_machine_data',
        'machine_data' : machine_json
        }
    
    channel_layer = get_channel_layer()
    
    async_to_sync(channel_layer.group_send)(group_name, message)
    
   