from django.shortcuts import render
from models import Trip, Visit, Place
from django.contrib.auth.models import User
from forms import MyForm

def index(request):
    context_dict ={}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'index.html', context_dict)


def plan(request):
    context_dict ={}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'plan.html', context_dict)

def about(request):
    context_dict ={}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'about.html', context_dict)

def explore(request):
    context_dict ={}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'explore.html', context_dict)

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

def add_trip(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = MyForm(request.POST)
        planner = User.objects.get(username='angelos')
        trip = Trip.objects.all()
        ftrip= None
        for trip1 in trip:
            print(trip1.planner.user_id)
            if (trip1.planner.user_id == planner.id):
                ftrip=trip1
        print(ftrip)
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            data = form.cleaned_data['places']
            for place in data:
                visit = Visit(trip=ftrip, place=place)
                visit.save()
                print(place)
            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = MyForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'add_trip.html', {'form': form})

