from django.db import models
from users.models import CustomUser

# Create your models here.
class Workspace(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    collaborators = models.ManyToManyField(CustomUser)