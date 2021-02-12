from django.test import TestCase
from model_mommy import mommy

# Create your tests here.
FILTER_LOCATION = 'bogota'
TEMPETURE = '2'


class ScubaDivingTestCase(TestCase):
    def setUp(self):
        dummy1 = mommy.make("scuba_dive_data.ScubaDiveData")
        dummy2 = mommy.make("scuba_dive_data.ScubaDiveData")
        dummy2.location = "Palmira"
        dummy1.location = "Cali"
        dummy2.water_temp = 0
        dummy2.outside_temp = 3
        dummy2.save()
        dummy1.save()

    def test_list(self):
        response = self.client.get(f'/scuba-dive-data/?search={FILTER_LOCATION}')
        data = response.json()
        print(data)
        self.assertEquals(len(data), 0)
        # self.assertEquals(data[0]['location'], 'Cali')
