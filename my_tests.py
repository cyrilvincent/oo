import unittest
import geometry as geo
import bank_account as ba

class My_Tests(unittest.TestCase):

    def test_rectangle_area(self):
        r1 = geo.Rectangle(3,2,geo.Point(0,0))
        self.assertEqual(6, r1.area)

    def test_rectangle_perimeter(self):
        r1 = geo.Rectangle(3,2,geo.Point(0,0))
        self.assertEqual(10, r1.perimeter)

    def test_account_robustness(self):
        a1 = ba.Account("01")
        with self.assertRaises(ValueError):
            a1.credit(-100)


    # def test_rectangle_area_error(self):
    #     r1 = geo.Rectangle(3,2,geo.Point(0,0))
    #     self.assertEqual(5, r1.area)