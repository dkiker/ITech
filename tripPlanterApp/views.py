from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response, redirect, get_object_or_404, render
from models import Trip, Visit, Place,Planner
from django.core.serializers.json import DjangoJSONEncoder

from django.core.urlresolvers import reverse,resolve
import json
from django.template.defaultfilters import slugify
from forms import MyForm,CreateTrip
from helper_functions import get_places,get_trip_list

def index(request):
    context_dict ={}
    # Sends a set with all the suggested trips to the index template as part of the context dictionary
    suggested_trips = Trip.objects.filter(isSuggestedTrip=True)
    context_dict['suggested_trips'] = suggested_trips
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'index.html', context_dict)



@login_required
def plan(request, location):

    print location

    print slugify(location)

    context_dict ={}
     # A HTTP POST?
    if request.method == 'POST':
        form = MyForm(request.POST)
        planner = Planner.objects.get(user=request.user)
        tripForm = CreateTrip(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid() and tripForm.is_valid():
            # Save the new category to the database.
            trip = tripForm.save(commit=False)
            trip.planner=planner #Planner will be sent automatically eventually
            trip.save()
            data = form.cleaned_data['places']
            for place in data:
                visit = Visit(trip=trip, place=place)
                visit.save()
            # Now call the index() view.
            # The user will be shown the homepage.
            return redirect(reverse('tripSummary', args=[trip.id] ))
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
            context_dict['errors'] = form.errors
    else:
        places = get_places(location)
        form = CreateTrip()
        # If the request was not a POST, display the form to enter details.
        context_dict['places'] = places
        context_dict['tripForm'] = form

    return render(request, 'plan.html', context_dict)

@login_required
def about(request):
    context_dict ={}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'about.html', context_dict)

@login_required
def explore(request):
    context_dict ={}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    suggested_trips = Trip.objects.filter(isSuggestedTrip=True)
    context_dict['trips'] = suggested_trips

    return render(request, 'explore.html', context_dict)

@login_required
def summary(request,tripID):

    print tripID
    context_dict ={}


    try:
        trip = Trip.objects.get(id=tripID)

        print trip.title
        context_dict['trip'] = trip

        visits = Visit.objects.filter(trip = trip)

        print visits
        context_dict['visits'] = visits

        places = []

        for visit in visits:
            place = Place.objects.get(id=visit.place.id)
            places.append(place)

        print places
        context_dict['places'] = places
    except Trip.DoesNotExist:
        pass

    return render(request,'summary.html',context_dict)



@login_required
def search_trips(request):

    if request.is_ajax():
        q = request.GET.get('term', '')
        trips = get_trip_list(20, q)
        results = []
        for trip in trips:
            trip_json = {}
            trip_json['id'] = trip.id
            trip_json['label'] = trip.title
            trip_json['value'] = trip.title
            results.append(trip_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)



@login_required
def mytrips(request):
    context_dict = {}
    context_dict['trips'] = Trip.objects.filter(planner=Planner.objects.get(user=request.user))

    return render(request, 'mytrips.html', context_dict)
#                markers.push({"type":"{{ place.type }}","description":"{{ place.description }}","id":{{ place.id }},
# "price":{{ place.price }},"name":"{{ place.name }}","position":{lat: {{ place.lat }} , lng: {{place.lon}}}});

@login_required
def add_location(request):
    response_data=[]

    if request.is_ajax():
        location = request.GET.get('location')
        places = get_places(location)
        for place in places:
            place_obj ={}
            place_obj['id'] = place.id
            place_obj['type'] = place.type
            place_obj['description'] = place.description
            place_obj['price'] = place.price
            place_obj['name'] = place.name
            place_obj['lat'] = place.lat
            place_obj['lng'] = place.lon
            response_data.append(place_obj)
    else:
        return HttpResponseBadRequest

    content_type = 'application/json'
    data = json.dumps(response_data, cls=DjangoJSONEncoder)

    return HttpResponse(data, content_type)