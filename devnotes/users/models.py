from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    username = None # we want email as login and django by default uses username for login, therefore remove it
    first_name = None
    last_name = None
    date_joined = None
    
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Set email as the unique identifier instead of username
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS are only used when you run python manage.py craetesuperuser
    REQUIRED_FIELDS = ['name']  # Required when creating a superuser
    # “When creating a superuser from the command line, ask for these additional fields besides USERNAME_FIELD and password.”