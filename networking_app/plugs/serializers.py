from rest_framework import serializers
from .models import PlugRequest, Message

class PlugRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlugRequest
        fields = ['id', 'magic_line', 'target_name', 'status', 'created_at']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'plug_request', 'content', 'timestamp']
