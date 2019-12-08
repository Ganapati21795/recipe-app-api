from django.test import TestCase
from app.calc import add, subtract


class CalcTests(TestCase):
    def test_add_numbers(self):
        """ tests that add two numbers """
        self.assertEqual(add(3, 1), 4)

    def test_subtact_numbers(self):
        """ tests that subtract two numbers """
        self.assertEqual(subtract(11, 5), 6)
