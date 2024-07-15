# main_1/models.py
from django.db import models

class Message(models.Model):
    text = models.TextField()
    x_position = models.IntegerField(default=0)
    y_position = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
