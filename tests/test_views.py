from django.test import TestCase
from restaurant.models import Menu
from django.test import *


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(ID = 5, Title = 'IceCream', Price = 8.00, Inventory = 16)
        Menu.objects.create(ID = 4, Title = 'MilkShake', Price = 5.00, Inventory = 17)

    def test_getall(self):
        response1 = self.client.get('/restaurant/menu/5')
        response2 = self.client.get('/restaurant/menu/')

        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response1.content.decode(), '{"ID":5,"Title":"IceCream","Price":"8.00","Inventory":16}')
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response2.content.decode(), '[{"ID":4,"Title":"MilkShake","Price":"5.00","Inventory":17},{"ID":5,"Title":"IceCream","Price":"8.00","Inventory":16}]')
        