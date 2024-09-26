from rest_framework import serializers
from .models import Machine, RealtimeData, DataLogs

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__'
        read_only_fields = ['identifier']

class RealtimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealtimeData
        fields = '__all__'
        
class DataLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataLogs
        fields = '__all__'