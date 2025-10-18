from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .serializers import UserSerializer
from django.contrib.auth.models import AbstractUser

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
class User(AbstractUser):
    email = models.EmailField(unique=True)