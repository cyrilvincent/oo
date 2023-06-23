import unittest

import config
import geometry as geo
import media
import bank
import csv
import pickle
import demo_singleton
import repository
import media_service as service


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
            total += m.net_price

    def test_cart(self):
        cart = media.Cart()
        b1 = media.Book("0", "Python", 10)
        cart.add(b1)
        cd1 = media.Cd("1", "Johnny", 20)
        cart.add(cd1)
        total = cart.total_net_price
        self.assertAlmostEqual(22.0325, total, delta=1e-3)
        with open("data/media/media.pickle", "wb") as f:
            pickle.dump(cart, f)

    def test_pickle_load(self):
        with open("data/media/media.pickle", "rb") as f:
            cart = pickle.load(f)
            self.assertEqual(2, len(cart.medias))

    def test_file(self):
        with open("data/house/house.csv", "r") as f:
            reader = csv.DictReader(f)
            total = 0
            count = 0
            for row in reader:
                total += float(row["loyer"]) / float(row["surface"])
                count += 1
            print(total / count)
            # calculer le prix /m² moyen dans un test

    # def test_load_csv(self):
    #     service = media.MediaService()
    #     service.load_csv("data/media/books.csv")
    #     self.assertEqual(4, len(service.medias))
    #     self.assertEqual("Python", service.medias[0].title)
    #     service.save_pickle("data/media/books.pickle")
    #
    # def test_load_pickle(self):
    #     service = media.MediaService()
    #     service.load_pickle("data/media/books.pickle")
    #     self.assertEqual(4, len(service.medias))
    #     self.assertEqual("Python", service.medias[0].title)
    #     service.save_csv("data/media/books2.csv")
    #     a1 = media.Author("Cyril", "Vincent")
    #     service.medias[0].authors.append(a1)
    #     service.save_json("data/media/books2.json")
    #     service.load_json("data/media/books2.json")
    #     self.assertEqual(4, len(service.medias))
    #
    # def test_load_xml(self):
    #     service = media.MediaService()
    #     service.load_xml("data/media/books.xml")
    #     self.assertEqual(2, len(service.medias))
    #     self.assertEqual("Python", service.medias[0].title)
    #
    # def test_save_xml(self):
    #     service = media.MediaService()
    #     service.load_pickle("data/media/books.pickle")
    #     service.save_xml("data/media/books.xml")
    #
    # def test_load_xl(self):
    #     service = media.MediaService()
    #     service.load_xl("data/media/books.xlsx")
    #     self.assertEqual(2, len(service.medias))

    def test_singleton(self):
        instance = demo_singleton.MediaServiceSingleton.get_instance()
        self.assertIsNotNone(instance)
        instance2 = demo_singleton.MediaServiceSingleton.get_instance()
        self.assertIs(instance, instance2)

    def test_csv_pickle_repository(self):
        pickle_repo = repository.BookPickleRepository("data/media/books.pickle")
        pickle_repo.load()
        csv_repo = repository.BookCSVRepository("data/media/books2.csv")
        csv_repo.medias = pickle_repo.medias
        csv_repo.save()

    def test_service_integration(self):
        s = service.MediaService()
        res = s.search("python")
        self.assertTrue(len(res) > 0)
        m = s.get_details(res[0].id)
        self.assertIsNotNone(m)
        s.add_media_to_cart(m)
        cart = s.get_cart()
        self.assertTrue(1, len(cart.medias))
        res = s.validate_cart()
        self.assertTrue(res)
        s.pay()

    def test_yield(self):
        repo = repository.BookCSVYieldRepository(config.default_path)
        medias = list(repo.medias)
        self.assertTrue(len(medias) > 0)

    def test_yield_title(self):
        repo = repository.BookCSVYieldRepository(config.default_path)
        medias = list(repo.get_by_title("python"))
        self.assertTrue(len(medias) > 0)

    def test_regex(self):
        isbn = "978-3-16-148410-0"
        book = media.Book(isbn, "", 0)
        with self.assertRaises(ValueError):
            book = media.Book(isbn+"X", "", 0)





