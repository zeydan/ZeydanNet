from django.db import models
from django.utils import timezone

class Message(models.Model):
    fullname = models.CharField(max_length=100)
    company =  models.CharField(max_length=100)
    email = models.EmailField(max_length=150, null=False)
    subject = models.CharField(max_length=150, null=False)
    message = models.TextField(max_length=1000, null=False)
    ipaddress = models.CharField(max_length=50)
    time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.email