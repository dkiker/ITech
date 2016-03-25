from models import Trip,Place
from django.template.defaultfilters import slugify


#Retrieves places filtered by the location
def get_places(location=''):
    places=[]
    if location:
                places = Place.objects.filter(locationSlug = slugify(location))

    return places



#Retrieves a number of trip objects
def get_trip_list(max_results=0, starts_with=''):
        trip_list = []
        if starts_with:
                trip_list = Trip.objects.filter(title__contains= starts_with)

        if max_results > 0:
                if trip_list.count() > max_results:
                        trip_list = trip_list[:max_results]

        return trip_list
