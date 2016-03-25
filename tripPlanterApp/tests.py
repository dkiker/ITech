from django.test import TestCase
from tripPlanterApp.models import Place,Trip,Planner
from django.core.urlresolvers import reverse
from django.test import Client
from django.contrib.auth.models import User

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

class PlaceTest(TestCase):

    def test_ensure_prices_are_positive(self):

        """
                make sure the prices are positive
        """
        place = add_place(name = "Exodus",
              type = 'R',
              location = "London",
              lat = 51.560820,
              lon = -0.098310,
              price = 20,
              description = "Exodus is all about contemporary Greek food culture, mind-blowing tastes together with the finest wines."
              )

        self.assertEqual((place.price >= 0), True)




class PlanViewTests(TestCase):
    #Setup a user
    def setUp(self):
            self.client = Client()
            self.user = User.objects.create_user('john', 'lennon', 'johnpassword')



    def test_plan_view(self):
        add_place(name = "Exodus",
              type = 'R',
              location = "Glasgow",
              lat = 51.560820,
              lon = -0.098310,
              price = 20,
              description = "Exodus is all about contemporary Greek food culture, mind-blowing tastes together with the finest wines."
              )

        add_place(name = "Rox Burger",
              type = 'R',
              location = "Glasgow",
              lat = 51.461301,
              lon = -0.006469,
              price = 11,
              description = "Rox Burger is a fun, new take on the gourmet burger industry."
              )
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('plan',kwargs={'location':'Glasgow'}),follow=True)#"follow" follows any redirects in case we are not logged in
        #Check for correct status code, returned form and places.
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Plan")
        self.assertNotEqual(response.context['tripForm'],None)
        num_places = len(response.context['places'])
        self.assertEqual(num_places, 2)

class IndexViewTests(TestCase):
    def setUp(self):
            self.client = Client()
            self.user = User.objects.create_user('john', 'lennon', 'johnpassword')
            planner = Planner.objects.get_or_create(user=self.user)[0]
            planner.country = "paradise?"
            planner.save()
    def test_index_view(self):
        add_trip(
        planner = Planner.objects.get(user=User.objects.get(username='john')),
        title = "Trip to Cardiff",
        isSuggestedTrip = True,
        )



        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        num_suggested = len(response.context['suggested_trips'])
        self.assertEqual(num_suggested,1)

