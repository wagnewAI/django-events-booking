from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    organizer_username = serializers.ReadOnlyField(source='organizer.username')

    class Meta:
        model = Event
        fields = [
            "id","organizer","organizer_username","title","description","location",
            "start_time","end_time","capacity","price","created_at","updated_at"
        ]
        read_only_fields = ["id","created_at","updated_at","organizer_username"]
