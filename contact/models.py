from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    age = models.IntegerField(blank=True)
    phone_number = models.CharField(max_length=15)
    date_created = models.DateTimeField(default=timezone.now)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"