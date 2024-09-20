from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/machine-realtime/(?P<machine_pk>\w+)/$', consumers.MachineRealtimeDataConsumer.as_asgi())
]