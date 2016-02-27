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
    title = models.CharField(unique=True,max_length=128)



class Place(models.Model):

    #decimals are very important in coordinates but using more than 6 is basically meaningless.
    name = models.CharField(max_length=128)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    price = models.IntegerField()


class Visit(models.Model):
    trip = models.ForeignKey(Trip)
    place = models.ForeignKey(Place)