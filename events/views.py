from django.shortcuts import render
from events.models import Event
from events.serializers import EventSerializer

from rest_framework import generics
    
class EventListView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
