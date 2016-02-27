from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Planner(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    country = models.CharField(blank=True,max_length=128)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class Trip(models.Model):
    planner = models.ForeignKey(Planner)
    title = models.CharField(max_length=128)

    def __unicode__(self):
        s = str(self.planner) + " - " + str(self.title)
        return s

class Place(models.Model):
    #decimals are very important in coordinates but using more than 6 is basically meaningless.
    name = models.CharField(max_length=128)
    lon = models.DecimalField(max_digits=9, decimal_places=6,blank=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6,blank=True)
    price = models.IntegerField()

    def __unicode__(self):
        return self.name

class Visit(models.Model):
    trip = models.ForeignKey(Trip)
    place = models.ForeignKey(Place)

    def __unicode__(self):
        s = str(self.trip) + " - " + str(self.place)
        return s