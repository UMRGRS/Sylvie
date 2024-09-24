from rest_framework import serializers
from .models import RealtimeData

class RealtimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealtimeData
        fields = '__all__'