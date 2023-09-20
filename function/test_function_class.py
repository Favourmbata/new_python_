from unittest import TestCase
from function import function_class


class Test(TestCase):
    def test_get_price(self):
        self.assertEqual(function_class.get_price(4), 2000)

    def test_get_price(self):
        self.assertEqual(function_class.get_price(9), 1800)

    def test_get_price(self):
        self.assertEqual(function_class.get_price(25), 1600)

    def test_get_price(self):
        self.assertEqual(function_class.get_price(45), 1500)

    def test_get_price(self):
        self.assertEqual(function_class.get_price(50), 1300)

    def test_get_price(self):
        self.assertEqual(function_class.get_price(120), 1200)

    def test_get_price(self):
        self.assertEqual(function_class.get_price(300), 1100)

    def test_get_price(self):
        self.assertEqual(function_class.get_price(700), 1000)
