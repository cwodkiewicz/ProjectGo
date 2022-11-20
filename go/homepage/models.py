from django.db import models

# Create your models here.

class Vacation(models.Model):
    destination_type = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    destination_weather = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.destination_type}, {self.destination}, {self.destination_weather}"