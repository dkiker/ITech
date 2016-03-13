import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TripPlanter.settings')

import django
django.setup()

from tripPlanterApp.models import Planner, Place, Trip,  Visit
from django.contrib.auth.models import User
from django.conf import settings

def populate():
    populate_planner()
    populate_place()
    populate_trip()
    populate_visit()

def populate_planner():

    add_planner(
        user = User.objects.create_superuser('angelos', 'angelos@apple.com', 'angelospassword'),
        country = "Cyprus"
    )

    add_planner(
        user = User.objects.create_superuser('dimitris', 'dimitris@kiker.com', 'dimitrispassword'),
        country = "Greece"
    )

    add_planner(
        user = User.objects.create_superuser('fotis', 'fotis@skeftikal.com', 'fotispassword'),
        country = "Cyprus"
    )

    add_planner(
        user = User.objects.create_superuser('zoe', 'zoe@ger.com', 'zoepassword'),
        country = "Cyprus"
    )

    add_planner(
        user = User.objects.create_superuser('leifos', 'leif@os.com', 'leifos'),
        country = "United Kingdom"
    )

    add_planner(
        user = User.objects.create_superuser('laura', 'laura@example.com', 'laura'),
        country = "United Kingdom"
    )

    add_planner(
        user = User.objects.create_superuser('david', 'david@max.com', 'david'),
        country = "United Kingdom"
    )

    for planner in Planner.objects.all():
        print "Planner - " + str(planner)


def populate_place():

    add_place(name = "Cardiff Castle",
              type = 'A',
              location = "Cardiff",
              lat = 51.481772,
              lon = -3.182204,
              price = 10,
              description = "Victorian Gothic fantasy built on the remains of Norman and Roman ruins, with a colourful interior."
              )

    add_place(name = "Cardiff Central Library",
              type = 'A',
              location = "Cardiff",
              lat = 51.477687,
              lon = -3.175362,
              price = 0,
              description = "Cardiff Central Library, is the main library in the city centre of Cardiff, Wales."
              )

    add_place(name = "Bute Park",
              type = 'A',
              location = "Cardiff",
              lat = 51.485111,
              lon = -3.185241,
              price = 0,
              description = "Bute Park is a major park in the city of Cardiff."
              )

    add_place(name = "National Museum Cardiff",
              type = 'A',
              location = "Cardiff",
              lat = 51.485886,
              lon = -3.177592,
              price = 0,
              description = "National Museum Cardiff is a museum and art gallery in Cardiff, Wales."
              )

    add_place(name = "Wales Millennium Centre",
              type = 'A',
              location = "Cardiff",
              lat = 51.464822,
              lon = -3.163151,
              price = 0,
              description = "Wales Millennium Centre is an arts centre located in the Cardiff Bay area of Cardiff, Wales."
              )

    add_place(name = "Elgano Hotel",
              type = 'H',
              location = "Cardiff",
              lat = 51.485980,
              lon = -3.194060,
              price = 84,
              description = "This modest B&B in a 4-storey Victorian brick townhouse is a 14-minute walk from Cardiff Castle."
              )

    add_place(name = "Jurys Inn Cardiff",
              type = 'H',
              location = "Cardiff",
              lat = 51.482784,
              lon = -3.173964,
              price = 84,
              description = "Formerly known as The Parc hotel, our Jurys Inn Cardiff hotel is conveniently located just a short walk from Cardiff Queen Street train station."
              )

    add_place(name = "The Avala Guesthouse",
              type = 'H',
              location = "Cardiff",
              lat = 51.489974,
              lon = -3.156957,
              price = 120,
              description = "In a stone-built Victorian house on a residential street, this laid-back guesthouse is 1.5 miles from medieval Cardiff Castle."
              )

    add_place(name = "The Royal Hotel Cardiff",
              type = 'H',
              location = "Cardiff",
              lat = 51.478065,
              lon = -3.178254,
              price = 43,
              description = "This historic Victorian building is Cardiff's oldest hotel, and is a 4-minute walk from both the Millennium Stadium."
              )

    add_place(name = "The St David's Hotel & Spa",
              type = 'H',
              location = "Cardiff",
              lat = 51.460550,
              lon = -3.167047,
              price = 87,
              description = "This upmarket, glass-fronted, waterside hotel is an 8-minute walk from the shops and restaurants at Mermaid Quay."
              )

    add_place(name = "Cafe Citta",
              type = 'R',
              location = "Cardiff",
              lat = 51.480479,
              lon = -3.179236,
              price = 10,
              description = "Family-run Italian cafe/restaurant with mother serving home-made dishes from its open kitchen."
              )

    add_place(name = "Coffee Barker",
              type = 'R',
              location = "Cardiff",
              lat = 51.480496,
              lon = -3.180522,
              price = 10,
              description = "Coffee Barker provides breakfast, dinner and tea to coffee lovers and city dwellers alike."
              )

    add_place(name = "Garlands",
              type = 'R',
              location = "Cardiff",
              lat = 51.481214,
              lon = -3.179776,
              price = 10,
              description = "Arty independent coffee shop/cafe serving traditional breakfasts and extravagant cakes."
              )

    add_place(name = "Milgi",
              type = 'R',
              location = "Cardiff",
              lat = 51.491838,
              lon = -3.171386,
              price = 10,
              description = "100% vegetarian restaurant, specialist in foraged foods, with a yurt outside for alternate dining."
              )

    add_place(name = "The Potted Pig",
              type = 'R',
              location = "Cardiff",
              lat = 51.480639,
              lon = -3.180733,
              price = 20,
              description = "Modern British cuisine with French and New York influences served in underground former bank vaults."
              )

    add_place(name = "Camera Obscura",
              type = 'A',
              location = "Edinburgh",
              lat = 55.948935,
              lon = -3.195755,
              price = 15,
              description = "Camera Obscura and World of Illusions is a major tourist attraction in the Old Town, Edinburgh, Scotland."
              )

    add_place(name = "Dynamic Earth",
              type = 'A',
              location = "Edinburgh",
              lat = 55.950533,
              lon = -3.1744,
              price = 0,
              description = "Dynamic Earth is a visitor attraction in Edinburgh, and also functions as a conference venue."
              )

    add_place(name = "Edinburgh Castle",
              type = 'A',
              location = "Edinburgh",
              lat = 55.948565,
              lon = -3.199881,
              price = 17,
              description = "Edinburgh Castle is an historic fortress which dominates the skyline of the city of Edinburgh, Scotland."
              )

    add_place(name = "National Museum of Scotland",
              type = 'A',
              location = "Edinburgh",
              lat = 55.946895,
              lon = -3.190488,
              price = 0,
              description = "Bright modern museum housing Scottish industrial history relics, natural history displays and cafe."
              )

    add_place(name = "Scott Monument",
              type = 'A',
              location = "Edinburgh",
              lat = 55.952381,
              lon = -3.193272,
              price = 0,
              description = "The Scott Monument is a Victorian Gothic monument to Scottish author Sir Walter Scott."
              )

    add_place(name = "Britannia Edinburgh Hotel",
              type = 'H',
              location = "Edinburgh",
              lat = 55.950561,
              lon = -3.222328,
              price = 29,
              description = "Set in the West End, this riverside hotel is a 10-minute walk from West Maitland Street bus stop."
              )

    add_place(name = "Brodies Hostels",
              type = 'H',
              location = "Edinburgh",
              lat = 55.950495,
              lon = -3.185907,
              price = 38,
              description = "Set on the Royal Mile, this budget option is spread over 2 buildings and is 5 minutes' walk from Edinburgh Waverley station."
              )

    add_place(name = "Edinburgh Lodge West End",
              type = 'H',
              location = "Edinburgh",
              lat = 55.945457,
              lon = -3.228969,
              price = 59,
              description = "In a traditional stone-built Victorian townhouse, this quaint hotel is a 7-minute walk from Edinburgh Haymarket railway station."
              )

    add_place(name = "Macdonald Holyrood Hotel",
              type = 'H',
              location = "Edinburgh",
              lat = 55.951028,
              lon = -3.177146,
              price = 76,
              description = "This modern hotel is a 3-minute walk from both Holyrood Park and the Royal Mile, and a 13-minute walk from Waverley train station."
              )

    add_place(name = "The Rutland Hotel",
              type = 'H',
              location = "Edinburgh",
              lat = 55.949969,
              lon = -3.207806,
              price = 157,
              description = "This upscale boutique hotel is a 1-minute walk from shopping on Princes Street."
              )

    add_place(name = "Field",
              type = 'R',
              location = "Edinburgh",
              lat = 55.944689,
              lon = -3.185446,
              price = 20,
              description = "Cow-themed, stripped-back fine-dining eatery for modern Scottish cuisine with pre-theatre option."
              )

    add_place(name = "Meze Meze",
              type = 'R',
              location = "Edinburgh",
              lat = 55.952480,
              lon = -3.199417,
              price = 15,
              description = "A Mediterranean Kitchen in the heart of Edinburgh."
              )

    add_place(name = "Reekie's Smokehouse",
              type = 'R',
              location = "Edinburgh",
              lat = 55.949294,
              lon = -3.182509,
              price = 17,
              description = "Scottish BBQ joint."
              )

    add_place(name = "Tapa",
              type = 'R',
              location = "Edinburgh",
              lat = 55.974691,
              lon = -3.170784,
              price = 35,
              description = "Authentic Spanish cuisine served tapas-style, with rioja and sangria, in tiled, Hispanic decor."
              )

    add_place(name = "Three Birds",
              type = 'R',
              location = "Edinburgh",
              lat = 55.936788,
              lon = -3.208072,
              price = 15,
              description = "Simple, contemporary dining room with a relaxed vibe, for Modern British dishes and sharing plates."
              )

    add_place(name = "Glasgow Gallery of Modern Art",
              type = 'A',
              location = "Glasgow",
              lat = 55.860113,
              lon = -4.252224,
              price = 0,
              description = "The Gallery of Modern Art is the main gallery of contemporary art in Glasgow, Scotland."
              )

    add_place(name = "Kelvingrove Art Gallery and Museum",
              type = 'A',
              location = "Glasgow",
              lat = 55.868613,
              lon = -4.290647,
              price = 0,
              description = "The Kelvingrove Art Gallery and Museum is a museum and art gallery in Glasgow, Scotland."
              )

    add_place(name = "Riverside Museum",
              type = 'A',
              location = "Glasgow",
              lat = 55.865181,
              lon = -4.306447,
              price = 0,
              description = "The Riverside Museum is the current location of the Glasgow Museum of Transport."
              )

    add_place(name = "The Lighthouse",
              type = 'A',
              location = "Glasgow",
              lat = 55.859534,
              lon = -4.255513,
              price = 0,
              description = "The Lighthouse in Glasgow is Scotland's Centre for Design and Architecture."
              )

    add_place(name = "The SSE Hydro",
              type = 'A',
              location = "Glasgow",
              lat = 55.860863,
              lon = -4.288135,
              price = 0,
              description = "The SSE Hydro is a multi-purpose indoor arena located on the site of the Scottish Exhibition and Conference Centre in Glasgow, Scotland."
              )

    add_place(name = "Belgrave Glasgow Hotel",
              type = 'H',
              location = "Glasgow",
              lat = 55.875809,
              lon = -4.283973,
              price = 35,
              description = "This basic hotel, in a Georgian building with an original staircase and framed photos of historic Glasgow, is a 6-minute walk from the nearest subway station and a 7-minute walk from the University of Glasgow."
              )

    add_place(name = "Glasgow Pond Hotel",
              type = 'H',
              location = "Glasgow",
              lat = 55.884374,
              lon = -4.310459,
              price = 67,
              description = "Overlooking Bingham's Pond and a 10-minute walk from the Hyndland railway station, this upscale hotel is 2 miles from the Kelvingrove Art Gallery and Museum."
              )

    add_place(name = "Heritage Hotel",
              type = 'H',
              location = "Glasgow",
              lat = 55.876557,
              lon = -4.286956,
              price = 57,
              description = "Heritage is located in the heart of North West district."
              )

    add_place(name = "Kelvin Hotel",
              type = 'H',
              location = "Glasgow",
              lat = 55.877437,
              lon = -4.287418,
              price = 39,
              description = "On a bustling West End street filled with shops and restaurants, this airy hotel is set in a row of Victorian townhouses."
              )

    add_place(name = "Lorne Hotel",
              type = 'H',
              location = "Glasgow",
              lat = 55.865492,
              lon = -4.284645,
              price = 58,
              description = "This modern hotel in a converted Victorian building is 0.6 miles from the University of Glasgow."
              )

    add_place(name = "Bread Meats Bread",
              type = 'R',
              location = "Glasgow",
              lat = 55.861571,
              lon = -4.256392,
              price = 10,
              description = "Industrial space with wooden furniture and large windows, for artisan burgers and BBQ sandwiches."
              )

    add_place(name = "Chaophraya",
              type = 'R',
              location = "Glasgow",
              lat = 55.862299,
              lon = -4.25377,
              price = 20,
              description = "Europe's largest Thai Restaurant"
              )

    add_place(name = "COSMO Restaurants",
              type = 'R',
              location = "Glasgow",
              lat = 55.822879,
              lon = -4.343346,
              price = 20,
              description = "Stylish, modern chain dining room with Pan-Asian cooking stations and global banquet options."
              )

    add_place(name = "Ketchup Westend",
              type = 'R',
              location = "Glasgow",
              lat = 55.87453,
              lon = -4.293269,
              price = 15,
              description = "Quirky venue with a vintage diner look and a fun vibe for kids, with dressing-up and party bags."
              )

    add_place(name = "The 78",
              type = 'R',
              location = "Glasgow",
              lat = 55.865069,
              lon = -4.286701,
              price = 15,
              description = "Retro vegetarian dining room with coal fire, comfy armchairs, chunky tables and French windows."
              )

    add_place(name = "Big Ben",
              type = 'A',
              location = "London",
              lat = 51.500733,
              lon = -0.124625,
              price = 0,
              description = "16-storey Gothic clocktower and national symbol at the Eastern end of the Houses of Parliament."
              )

    add_place(name = "Buckingham Palace",
              type = 'A',
              location = "London",
              lat = 51.501337,
              lon = -0.141847,
              price = 0,
              description = "Buckingham Palace is the London residence and principal workplace of the reigning monarch of the United Kingdom."
              )

    add_place(name = "London Eye",
              type = 'A',
              location = "London",
              lat = 51.503344,
              lon = -0.119543,
              price = 0,
              description = "Huge observation wheel giving passengers a privileged bird's-eye view of the city's landmarks."
              )

    add_place(name = "Madame Tussauds",
              type = 'A',
              location = "London",
              lat = 51.522890,
              lon = -0.154967,
              price = 24,
              description = "Madame Tussauds is a wax museum in London with branches in a number of major cities."
              )

    add_place(name = "Westminster Abbey",
              type = 'A',
              location = "London",
              lat = 51.499265,
              lon = -0.127224,
              price = 0,
              description = "Westminster Abbey is a large, mainly Gothic abbey church in the City of Westminster, London."
              )

    add_place(name = "Amba Hotel Marble Arch",
              type = 'H',
              location = "London",
              lat = 51.514259,
              lon = -0.156547,
              price = 148,
              description = "Set in an art deco building, this grand hotel overlooks Oxford Street and Hyde Park."
              )

    add_place(name = "Apex Temple Court Hotel",
              type = 'H',
              location = "London",
              lat = 51.513730,
              lon = -0.108918,
              price = 140,
              description = "Around a courtyard off Fleet Street, this upscale redbrick hotel is a 5-minute walk from City Thameslink train station."
              )

    add_place(name = "The Langham London",
              type = 'H',
              location = "London",
              lat = 51.517428,
              lon = -0.143232,
              price = 302,
              description = "Hosting guests since 1865, this chic Victorian hotel is 3 blocks from Oxford Street shopping."
              )

    add_place(name = "The Marylebone Hotel",
              type = 'H',
              location = "London",
              lat = 51.518012,
              lon = -0.149805,
              price = 189,
              description = "Set among the trendy shops & restaurants of Marylebone Village, this modern, upscale hotel is a 13-minute walk from Baker Street Tube station."
              )

    add_place(name = "The May Fair Hotel",
              type = 'H',
              location = "London",
              lat = 51.507978,
              lon = -0.143846,
              price = 216,
              description = "This luxury hotel, opened by King George V in 1927, is a 3-minute walk from Green Park tube station."
              )

    add_place(name = "Bar 61 Restaurant",
              type = 'R',
              location = "London",
              lat = 51.440021,
              lon = -0.125527,
              price = 25,
              description = "Bar with vintage dark-wood decor and stripped floor, plus Modern European and tapas dining."
              )

    add_place(name = "Cereal Killer Cafe",
              type = 'R',
              location = "London",
              lat = 51.523919,
              lon = -0.071617,
              price = 5,
              description = "Colourful, nostalgic eatery with more than 120 cereals, plus a selection of milk and toppings."
              )

    add_place(name = "Comedor Grill & Bar",
              type = 'R',
              location = "London",
              lat = 51.541573,
              lon = -0.103093,
              price = 30,
              description = "Pan-South American cuisine served in a contemporary rustic dining room hung with abstract paintings."
              )

    add_place(name = "Exodus",
              type = 'R',
              location = "London",
              lat = 51.560820,
              lon = -0.098310,
              price = 20,
              description = "Exodus is all about contemporary Greek food culture, mind-blowing tastes together with the finest wines."
              )

    add_place(name = "Rox Burger",
              type = 'R',
              location = "London",
              lat = 51.461301,
              lon = -0.006469,
              price = 11,
              description = "Rox Burger is a fun, new take on the gourmet burger industry."
              )

    for place in Place.objects.all():
        print "Place - " + str(place)


def populate_trip():

    media_url = settings.MEDIA_URL

    add_trip(
        planner = Planner.objects.get(user=User.objects.get(username='dimitris')),
        title = "Trip to Cardiff",
        isSuggestedTrip = True,
        photograph = media_url + 'trip_images/cardiff-castle.jpeg'
    )

    add_trip(
        planner = Planner.objects.get(user=User.objects.get(username='fotis')),
        title = "Trip to Edinburgh",
        isSuggestedTrip = True,
        photograph = media_url + 'trip_images/our-dynamic-earth.jpeg'
    )

    add_trip(
        planner = Planner.objects.get(user=User.objects.get(username='angelos')),
        title = "Trip to Glasgow",
        isSuggestedTrip = True,
        photograph = media_url + 'trip_images/hydro.jpeg'
    )

    add_trip(
        planner = Planner.objects.get(user=User.objects.get(username='zoe')),
        title = "Trip to London",
        isSuggestedTrip = True,
        photograph = settings.MEDIA_URL + 'trip_images/london-eye.jpeg'
    )

    for trip in Trip.objects.all():
        print "Trip - " + str(trip)


def populate_visit():

    add_visit(
        trip = Trip.objects.get(planner=Planner.objects.get(user=User.objects.get(username='dimitris')), title='Trip to Cardiff'),
        place = Place.objects.get(name='Cardiff Castle'),
    )

    add_visit(
        trip = Trip.objects.get(planner=Planner.objects.get(user=User.objects.get(username='dimitris')), title='Trip to Cardiff'),
        place = Place.objects.get(name='Jurys Inn Cardiff'),
    )

    add_visit(
        trip = Trip.objects.get(planner=Planner.objects.get(user=User.objects.get(username='dimitris')), title='Trip to Cardiff'),
        place = Place.objects.get(name='Garlands'),
    )

    add_visit(
        trip = Trip.objects.get(planner=Planner.objects.get(user=User.objects.get(username='fotis')), title='Trip to Edinburgh'),
        place = Place.objects.get(name='Camera Obscura'),
    )

    add_visit(
        trip = Trip.objects.get(planner=Planner.objects.get(user=User.objects.get(username='fotis')), title='Trip to Edinburgh'),
        place = Place.objects.get(name='Britannia Edinburgh Hotel'),
    )

    add_visit(
        trip = Trip.objects.get(planner=Planner.objects.get(user=User.objects.get(username='fotis')), title='Trip to Edinburgh'),
        place = Place.objects.get(name='Reekie\'s Smokehouse'),
    )

    add_visit(
        trip = Trip.objects.get(planner=Planner.objects.get(user=User.objects.get(username='angelos')), title='Trip to Glasgow'),
        place = Place.objects.get(name='The SSE Hydro'),
    )

    add_visit(
        trip = Trip.objects.get(planner=Planner.objects.get(user=User.objects.get(username='angelos')), title='Trip to Glasgow'),
        place = Place.objects.get(name='Heritage Hotel'),
    )

    add_visit(
        trip = Trip.objects.get(planner=Planner.objects.get(user=User.objects.get(username='angelos')), title='Trip to Glasgow'),
        place = Place.objects.get(name='Bread Meats Bread'),
    )

    add_visit(
        trip = Trip.objects.get(planner=Planner.objects.get(user=User.objects.get(username='zoe')), title='Trip to London'),
        place = Place.objects.get(name='London Eye'),
    )

    add_visit(
        trip = Trip.objects.get(planner=Planner.objects.get(user=User.objects.get(username='zoe')), title='Trip to London'),
        place = Place.objects.get(name='Apex Temple Court Hotel'),
    )

    add_visit(
        trip = Trip.objects.get(planner=Planner.objects.get(user=User.objects.get(username='zoe')), title='Trip to London'),
        place = Place.objects.get(name='Cereal Killer Cafe'),
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


def add_trip(planner, title, isSuggestedTrip, photograph):
    trip = Trip.objects.get_or_create(planner=planner, title=title)[0]
    trip.isSuggestedTrip = isSuggestedTrip
    trip.photograph = photograph
    trip.save()
    return trip


def add_visit(trip, place):
    visit = Visit.objects.get_or_create(trip=trip, place=place)[0]


if __name__ == '__main__':
    print "Starting TripPlanter Population Script..."
    populate()














