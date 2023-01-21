from django.test import TestCase
from restaurant.models import Menu
from django.test import *


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(ID = 3, Title = 'Fried Chicken', Price = 18.00, Inventory = 11)
        self.assertEquals(str(item), "Fried Chicken : 18.0")




