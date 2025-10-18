from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User  # Or .models.User

admin.site.register(User)