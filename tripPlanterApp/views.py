from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from models import Trip, Visit, Place


def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'index.html', context_dict)


def summary(request,tripID):

    context_dict ={}


    try:
        trip = Trip.objects.get(id=tripID)

        context_dict['trip'] = trip

        visits = Visit.objects.filter(trip = trip)

        context_dict['visits'] = visits

        places = []

        for visit in visits:
            place = Place.objects.get(id=visit.place.id)
            places.append(place)

        context_dict['places'] = places
    except Trip.DoesNotExist:
        pass

    return render(request,'summary.html',context_dict)


