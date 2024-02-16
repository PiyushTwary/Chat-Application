from django.db import models

# Create your models here.
class Room(models.Model):
    room_name = models.CharField(max_length=250)
    

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    sender = models.CharField(max_length=250)
    message = models.TextField()
    