import unittest
from typing import List

import geometry as geo
import bank_account as ba
import media
import device
import csv
import pickle
import jsonpickle
import openpyxl
import repositories

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
        with open("data/media/books.pickle", "wb") as f:
            pickle.dump(books, f)

    def test_pickle(self):
        with open("data/media/books.pickle", "rb") as f:
            books = pickle.load(f)
            print(books)

    def test_jsonpickle(self):
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
        with open("data/media/books2.json", "w") as f:
            s = jsonpickle.dumps(books)
            f.write(s)

    def test_xl(self):
        workbook = openpyxl.open("data/media/books.xlsx")
        sheet = workbook.worksheets[0]
        title = sheet.cell(2,2).value
        self.assertEqual("Python", title)

    def test_singleton(self):
        instance = media.Singleton.get_instance()
        instance2 = media.Singleton.get_instance()
        self.assertIs(instance, instance2)

    def test_repository(self):
        repo = repositories.BookCsvRepository("data/media/books.csv")
        repo.load()
        book = repo.get_by_id("1")
        self.assertIsNotNone(book)
        self.assertEqual("Python", book.title)
        repo_pickle = repositories.BookPickleRepository("data/media/books.pickle")
        repo_pickle.medias = repo.medias
        repo_pickle.save()

    def test_isbn(self):
        s = "978-0-13-601970-1"
        book = media.Book(s, "", 0, None)
        self.assertTrue(book.validate_isbn(s))
        s = "9780-13-601-970-1"
        self.assertFalse(book.validate_isbn(s))



