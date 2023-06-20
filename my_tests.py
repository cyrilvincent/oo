import unittest
import geometry as geo
import media

class DemoTest(unittest.TestCase):

    def test_square_area(self):
        s1 = geo.Square(3)
        self.assertEqual(8, s1.area)

    def test_net_price(self):
        b1 = media.Book("","",10)
        self.assertEqual(10.55, b1.net_price())

