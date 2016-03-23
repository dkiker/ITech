from django.test import TestCase
from tripPlanterApp.models import Place

class PlaceTest(TestCase):

    def test_ensure_prices_are_positive(self):

        """
                make sure the prices are positive
        """
        place = Place.objects.get_or_create(name="Ketchup Westend", lat=55.87453, lon=-4.293269, price=-15)[0]
        place.type = 'R'
        place.location = "Glasgow"
        place.description = "Quirky venue with a vintage diner look and a fun vibe for kids, with dressing-up and party bags."
        place.save()
        self.assertEqual((place.price >= 0), True)




