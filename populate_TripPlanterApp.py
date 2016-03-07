import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TripPlanter.settings')

import django
django.setup()

from tripPlanterApp.models import Planner, Place, Trip,  Visit
from django.contrib.auth.models import User

def populate():
    populate_planner()
    populate_place()
    populate_trip()
    populate_visit()

def populate_planner():

    add_planner(
        user = User.objects.create_user('angelos', 'angelos@apple.com', 'angelospassword'),
        country = "Cyprus"
    )

    add_planner(
        user = User.objects.create_user('dimitris', 'dimitris@kiker.com', 'dimitrispassword'),
        country = "Greece"
    )

    add_planner(
        user = User.objects.create_user('fotis', 'fotis@skeftikal.com', 'fotispassword'),
        country = "Cyprus"
    )

    add_planner(
        user = User.objects.create_user('zoe', 'zoe@ger.com', 'zoepassword'),
        country = "Cyprus"
    )

    for planner in Planner.objects.all():
        print "Planner - " + str(planner)

def populate_place():

    add_place(name = "London Eye",
              type = 'A',
              location = "London",
              lat = 51.503344,
              lon = -0.119543,
              price = 0,
              description = "Huge observation wheel giving passengers a privileged bird's-eye view of the city's landmarks."
              )

    add_place(name = "Cardiff Castle",
              type = 'A',
              location = "Cardiff",
              lat = 51.481772,
              lon = -3.182204,
              price = 10,
              description = "Victorian Gothic fantasy built on the remains of Norman and Roman ruins, with a colourful interior."
              )

    add_place(name = "Dynamic Earth",
              type = 'A',
              location = "Edinburgh",
              lat = 55.950533,
              lon = -3.1744,
              price = 0,
              description = "Dynamic Earth is a visitor attraction in Edinburgh, and also functions as a conference venue."
              )

    add_place(name = "The SSE Hydro",
              type = 'A',
              location = "Glasgow",
              lat = 55.860863,
              lon = -4.288135,
              price = 0,
              description = "The SSE Hydro is a multi-purpose indoor arena located on the site of the Scottish Exhibition and Conference Centre in Glasgow, Scotland."
              )

    add_place(name = "Glasgow Gallery of Modern Art",
              type = 'A',
              location = "Glasgow",
              lat = 55.860113,
              lon = -4.252224,
              price = 0,
              description = "The Gallery of Modern Art is the main gallery of contemporary art in Glasgow, Scotland."
              )

    add_place(name = "Chaophraya",
              type = 'R',
              location = "Glasgow",
              lat = 55.862299,
              lon = -4.25377,
              price = 20,
              description = "Europe's largest Thai Restaurant"
              )

    add_place(name = "Ketchup Westend",
              type = 'R',
              location = "Glasgow",
              lat = 55.87453,
              lon = -4.293269,
              price = 15,
              description = "Quirky venue with a vintage diner look and a fun vibe for kids, with dressing-up and party bags."
              )

    add_place(name = "Bread Meats Bread",
              type = 'R',
              location = "Glasgow",
              lat = 55.861571,
              lon = -4.256392,
              price = 10,
              description = "Industrial space with wooden furniture and large windows, for artisan burgers and BBQ sandwiches."
              )

    for place in Place.objects.all():
        print "Place - " + str(place)

def populate_trip():

    add_trip(
        planner = Planner.objects.get(user=User.objects.get(username='angelos')),
        title = "Trip to Glasgow",
        isSuggestedTrip = True
    )

    add_trip(
        planner = Planner.objects.get(user=User.objects.get(username='dimitris')),
        title = "Trip to Cardiff",
        isSuggestedTrip = True
    )

    add_trip(
        planner = Planner.objects.get(user=User.objects.get(username='fotis')),
        title = "Trip to Edinburgh",
        isSuggestedTrip = True
    )

    add_trip(
        planner = Planner.objects.get(user=User.objects.get(username='zoe')),
        title = "Trip to London",
        isSuggestedTrip = True
    )

    for trip in Trip.objects.all():
        print "Trip - " + str(trip)

def populate_visit():

    add_visit(
        trip = Trip.objects.get(planner=Planner.objects.get(user=User.objects.get(username='angelos')), title='Trip to Glasgow'),
        place = Place.objects.get(name='Ketchup Westend'),
    )

    add_visit(
        trip = Trip.objects.get(planner=Planner.objects.get(user=User.objects.get(username='angelos')), title='Trip to Glasgow'),
        place = Place.objects.get(name='Bread Meats Bread'),
    )

    for visit in Visit.objects.all():
        print "Visit - " + str(visit)

def add_planner(user, country):
    planner = Planner.objects.get_or_create(user=user)[0]
    planner.country = country
    planner.save()
    return planner

def add_place(name, type, location, lat, lon, price, description):
    place = Place.objects.get_or_create(name=name, lat=lat, lon=lon, price=price)[0]
    place.type = type
    place.location = location
    place.description = description
    place.save()
    return place

def add_trip(planner, title, isSuggestedTrip):
    trip = Trip.objects.get_or_create(planner=planner, title=title)[0]
    trip.isSuggestedTrip = isSuggestedTrip
    trip.save()
    return trip

def add_visit(trip, place):
    visit = Visit.objects.get_or_create(trip=trip, place=place)[0]

if __name__ == '__main__':
    print "Starting TripPlanter Population Script..."
    populate()




















