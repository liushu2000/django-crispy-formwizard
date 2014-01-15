from django.db import models
import datetime
from django.contrib.auth.models import User


class Contact(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=40)
    phone = models.IntegerField(blank=True, null=True, max_length=12)
    #vehicle_type = models.ForeignKey(Vehicle_Type)
    memo = models.CharField(blank=True, null=True, max_length=200)
    location = models.CharField(blank=True, null=True, max_length=20)
    created_at = models.DateTimeField(blank=True, null=True, default=datetime.datetime.now())

    def __unicode__(self):
        return self.name

    # def get_absolute_url(self):
    #
    #     return "user-{pk}".format(pk=self.pk)


class Contact_Revision(models.Model):
    revision_number = models.CharField(primary_key=True, max_length = 100)
    Contact = models.ForeignKey(Contact)
    def __unicode__(self):
        return self.revision_number