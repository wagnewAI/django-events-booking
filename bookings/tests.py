from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from events.models import Event
from .models import Booking
from django.urls import reverse
import datetime

class BookingTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('booker', 'booker@example.com', 'pass')
        self.admin = User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')
        self.client.force_authenticate(user=self.user)
        self.event = Event.objects.create(name='Event', date=datetime.datetime.now(), venue='Venue', capacity=100)

    def test_make_booking(self):
        url = '/api/bookings/'
        data = {'event_id': self.event.id, 'seats_booked': 2}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)
        self.event.refresh_from_db()
        self.assertEqual(self.event.available_seats, 98)

    def test_booking_exceeds_capacity(self):
        self.event.capacity = 1
        self.event.save()
        url = '/api/bookings/'
        data = {'event_id': self.event.id, 'seats_booked': 2}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cancel_booking(self):
        booking = Booking.objects.create(user=self.user, event=self.event, seats_booked=2)
        url = f'/api/bookings/{booking.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.event.refresh_from_db()
        self.assertEqual(self.event.available_seats, 100)  # Restored