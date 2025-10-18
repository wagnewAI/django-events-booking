from rest_framework import serializers
from .models import Booking
from events.models import Event
from decimal import Decimal

class BookingSerializer(serializers.ModelSerializer):
    user_username = serializers.ReadOnlyField(source='user.username')
    event_title = serializers.ReadOnlyField(source='event.title')

    class Meta:
        model = Booking
        fields = ["id","user","user_username","event","event_title","quantity","total_amount","status","created_at"]
        read_only_fields = ["id","total_amount","status","created_at","user_username","event_title"]

    def validate(self, data):
        event = data.get("event")
        quantity = data.get("quantity", 1)
        if event.start_time <= timezone.now():
            raise serializers.ValidationError("Cannot book past events.")
        if quantity <= 0:
            raise serializers.ValidationError("Quantity must be at least 1.")
        if event.capacity < quantity:
            raise serializers.ValidationError("Not enough capacity.")
        return data

    def create(self, validated_data):
        user = self.context['request'].user
        event = validated_data['event']
        quantity = validated_data['quantity']

        # concurrency-safe decrement
        from django.db import transaction
        from django.db.models import F

        with transaction.atomic():
            ev = Event.objects.select_for_update().get(pk=event.pk)
            if ev.capacity < quantity:
                raise serializers.ValidationError("Not enough capacity.")
            ev.capacity = F('capacity') - quantity
            ev.save(update_fields=['capacity'])
            ev.refresh_from_db()

            total = Decimal(ev.price) * Decimal(quantity)
            booking = Booking.objects.create(
                user=user,
                event=ev,
                quantity=quantity,
                total_amount=total,
                status=Booking.CONFIRMED
            )
        return booking
