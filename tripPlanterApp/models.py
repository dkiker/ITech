from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from registration.signals import  user_registered
from django.dispatch import receiver
from django.core.exceptions import ValidationError

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
    photograph = models.ImageField(upload_to='trip_images', blank=True,default='trip_images/default.png')
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
    price = models.IntegerField(blank=True)
    description = models.CharField(max_length=250, default="")
    locationSlug = models.SlugField()

    def save(self, *args, **kwargs):
        # Uncomment if you don't want the slug to change every time the name changes
        #if self.id is None:
        #self.slug = slugify(self.name)
        if (self.price < 0):
            self.price = self.price * -1
        self.locationSlug = slugify(self.location)
        super(Place, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class Visit(models.Model):
    trip = models.ForeignKey(Trip)
    place = models.ForeignKey(Place)

    def __unicode__(self):
        s = str(self.trip) + " - " + str(self.place)
        return s

#This method is called after a new user registers. It is used to create a new Planner
@receiver(user_registered)
def callback(sender, **kwargs):
    user = kwargs.pop('user')
    planner = Planner.objects.get_or_create(user=user)[0]
    planner.save()


