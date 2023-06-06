import unittest
import geometry as geo

class My_Tests(unittest.TestCase):

    def test_rectangle_area(self):
        r1 = geo.Rectangle(3,2,geo.Point(0,0))
        self.assertEqual(6, r1.area)

    def test_rectangle_perimeter(self):
        r1 = geo.Rectangle(3,2,geo.Point(0,0))
        self.assertEqual(10, geo.perimeter)

    # def test_rectangle_area_error(self):
    #     r1 = geo.Rectangle(3,2,geo.Point(0,0))
    #     self.assertEqual(5, r1.area)