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
    photograph = models.ImageField(upload_to='trip_images', blank=True)
    isSuggestedTrip = models.BooleanField(default=False)

    def __unicode__(self):
        s = str(self.planner) + " - " + str(self.title)
        return s

class Place(models.Model):
    # Defines the choices for the 'type' field
    ATTRACTION = 'A'
    HOTEL = 'H'
    RESTAURANT = 'R'

    TYPE_CHOICES = (
        (ATTRACTION, 'Attraction'),
        (HOTEL, 'Hotel'),
        (RESTAURANT, 'Restaurant'),
    )

    #decimals are very important in coordinates but using more than 6 is basically meaningless.
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    location = models.CharField(max_length=20)
    lat = models.DecimalField(max_digits=9, decimal_places=6,blank=True)
    lon = models.DecimalField(max_digits=9, decimal_places=6,blank=True)
    price = models.IntegerField()
    description = models.CharField(max_length=150, default="")

    def __unicode__(self):
        return self.name

class Visit(models.Model):
    trip = models.ForeignKey(Trip)
    place = models.ForeignKey(Place)

    def __unicode__(self):
        s = str(self.trip) + " - " + str(self.place)
        return s