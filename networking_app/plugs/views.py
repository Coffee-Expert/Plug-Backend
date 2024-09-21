from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import PlugRequest, Message
from .serializers import PlugRequestSerializer, MessageSerializer

class PlugRequestViewSet(viewsets.ModelViewSet):
    queryset = PlugRequest.objects.all()   
    serializer_class = PlugRequestSerializer   

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()   
    serializer_class = MessageSerializer  
