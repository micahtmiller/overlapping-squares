import unittest
import overlapping_squares as os


class TestOverlappingSquares(unittest.TestCase):
    def test_mapping(self):
        rect1 = os.Rectangle(os.Points(0, 5), os.Points(5, 0))
        rect2 = os.Rectangle(os.Points(10, 5), os.Points(15, 0))

        rect_list = [rect1, rect2]
        expected = {rect1: [rect2], rect2: [rect1]}
        self.assertEqual(expected, os.create_mapping(rect_list))
        # self.assertTrue(False)
