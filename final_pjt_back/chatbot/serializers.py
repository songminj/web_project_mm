from rest_framework import serializers
from .models import ChatBot

class ChatBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatBot
        fields = '__all__'
        read_only_fields = ('user',)