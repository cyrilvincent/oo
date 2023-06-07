import unittest
from typing import List

import geometry as geo
import bank_account as ba
import media
import device
import csv

class My_Tests(unittest.TestCase):

    def test_rectangle_area(self):
        r1 = geo.Rectangle(geo.Point(0,0),3,2)
        self.assertEqual(6, r1.area)

    def test_rectangle_perimeter(self):
        r1 = geo.Rectangle(geo.Point(0,0),3,2)
        self.assertEqual(10, r1.perimeter)

    def test_square_area(self):
        r1 = geo.Square(3, geo.Point(0,0))
        self.assertEqual(9, r1.area)

    def test_account_robustness(self):
        a1 = ba.Account("01")
        with self.assertRaises(ValueError):
            a1.credit(-100)

    def test_abstract(self):
        # p = geo.Polygon(geo.Point(0,0))
        # print(p)
        l = geo.Losange(geo.Point(0,0))
        print(l)

    def test_polymorphisme(self):
        l: List[geo.Polygon] = []
        l.append(geo.Rectangle(geo.Point(0,0),3,2))
        l.append(geo.Square(3, geo.Point(0, 0)))
        l.append(geo.Losange(geo.Point(0, 0)))
        for polygon in l:
            print(polygon.area)

    def test_cart(self):
        c = media.Cart([])
        c.add(media.Book("1", "Python", 10, None))
        c.add(media.Cd("2", "Johnny", 20, None))
        price = c.net_price
        self.assertAlmostEqual(26.785, price,delta=1e-3)

    def test_device(self):
        dev = device.VoltmetreMockB()
        service = device.Service(dev)
        service.start(10)
        self.assertEqual(10, len(dev.mesures))
        self.assertEqual(0.01, dev.mesures[1].value)

    def test_csv(self):
        books = []
        with open("data/media/books.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                id = row["id"]
                title = row["title"]
                price = float(row["price"])
                book = media.Book(id,title,price,None)
                books.append(book)
        print(books)



    # def test_rectangle_area_error(self):
    #     r1 = geo.Rectangle(3,2,geo.Point(0,0))
    #     self.assertEqual(5, r1.area)