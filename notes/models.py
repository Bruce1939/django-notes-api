from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Note(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
