from django.test import TestCase
from app.calc import add



class CalcTests(TestCase):
    def test_add_numbers(self):
        """ tests that add two numbers """
        self.assertEqual(add(3, 1), 4)
        