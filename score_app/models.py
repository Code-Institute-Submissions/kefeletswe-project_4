from django.db import models

# Create your models here.
class Participants(models.Model):
    participant_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=50)
    age = models.PositiveIntegerField(null=True, blank=True)

def __str__(self):
  return f'Participants: {self.first_name} {self.last_name}'