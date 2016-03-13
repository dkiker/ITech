from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404, render
from models import Trip, Visit, Place,Planner
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse,resolve
import json
from django.template.defaultfilters import slugify
from forms import MyForm,CreateTrip

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
        print(request.POST)
        form = MyForm(request.POST)
        print(request.user)
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
                print(place)
            # Now call the index() view.
            # The user will be shown the homepage.
            return redirect(reverse('tripSummary', args=[trip.id] ))
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
            context_dict['errors'] = form.errors
    else:
        places = Place.objects.filter(locationSlug = slugify(location))#WILL BE FILTERED BY LOCATION SELECTED
        form = CreateTrip()
        # If the request was not a POST, display the form to enter details.
        context_dict['places'] = places
        context_dict['tripForm'] = form
        print(form)

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
        trips = Trip.objects.filter(title__contains= q )[:20]
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
