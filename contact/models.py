from django.db import models
import datetime

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    phone = models.CharField(blank=True, null=True, max_length=12)
    #vehicle_type = models.ForeignKey(Vehicle_Type)
    memo = models.CharField(blank=True, null=True, max_length=200)
    location = models.CharField(blank=True, null=True, max_length=20)
    created_at = models.DateTimeField(blank=True, null=True, default=datetime.datetime.now())
