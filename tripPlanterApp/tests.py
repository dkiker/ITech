from django.test import TestCase
from tripPlanterApp.models import Place
from django.core.urlresolvers import reverse
from django.test import Client
from django.contrib.auth.models import User
from forms import CreateTrip
def add_place(name, type, location, lat, lon, price, description):
    place = Place.objects.get_or_create(name=name, lat=lat, lon=lon, price=price)[0]
    place.type = type
    place.location = location
    place.description = description
    place.save()
    return place


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
        response = self.client.get(reverse('plan',kwargs={'location':'Glasgow'}),follow=True)
        #Check if we are not logged in
        print(response.redirect_chain)
        #Check for correct status code, returned form and places.
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Plan")
        self.assertNotEqual(response.context['tripForm'],None)
        num_places = len(response.context['places'])
        self.assertEqual(num_places, 2)

