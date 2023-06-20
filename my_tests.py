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

    def test_polymorphism(self):
        m:media.Media = media.Book("","",0)
        # b:media.Book = media.Media("","",0)

    def test_list_polymorphism(self):
        medias = [
            media.Book("0", "Python", 10),
            media.Cd("1", "Johnny", 20)
        ]
        total = 0
        for m in medias:
            total += m.net_price()

    def test_cart(self):
        cart = media.Cart()
        b1 = media.Book("0", "Python", 10)
        cart.add(b1)
        cd1 = media.Cd("1", "Johnny", 20)
        cart.add(cd1)
        total = cart.total_net_price
        self.assertAlmostEqual(20.1234, total, delta=1e-3)


