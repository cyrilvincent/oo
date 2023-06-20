import unittest
import geometry as geo
import media
import bank

class DemoTest(unittest.TestCase):

    def test_square_area(self):
        s1 = geo.Square(3)
        self.assertEqual(8, s1.area)

    def test_net_price(self):
        b1 = media.Book("","",10)
        self.assertAlmostEqual(10.55, b1.net_price(),delta=1e-3)

    def test_negative_credit(self):
        with self.assertRaises(ValueError):
            a1 = bank.BankAccount("0")
            a1.credit(-1)