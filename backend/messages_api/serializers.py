from rest_framework import serializers
from messages_api.models import Message


class MessageSerializer(serializers.Serializer):
    class Meta:
        model = Message
        fields = ("id", "api", "text", "branch")
