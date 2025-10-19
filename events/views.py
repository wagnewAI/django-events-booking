from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Event
from .serializers import EventSerializer

class IsOrganizerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.organizer == request.user or request.user.is_staff

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.select_related("organizer").all()
    serializer_class = EventSerializer
    permission_classes = [IsOrganizerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)
