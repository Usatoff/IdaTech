import unittest
from app.subject import Subject, MIN_VALUE, MAX_VALUE, _move_in_range, _intervals_intersection


class TestSubjectFunctions(unittest.TestCase):
    """test functions from ..app.subject"""

    def test_move_in_range_from_left(self):

        too_small_value = 0

        self.assertEqual(_move_in_range(too_small_value), MIN_VALUE)

    def test_move_in_range_from_right(self):
        too_big_value = 10

        self.assertEqual(_move_in_range(too_big_value), MAX_VALUE)

    def test_intervals_intersection_common_part(self):
        a1, b1, a2, b2 = 0, 5, 3, 10

        self.assertEqual(_intervals_intersection(a1, b1, a2, b2), 2)

    def test_intervals_intersection_one_in_another(self):
        a1, b1, a2, b2 = 0, 10, 2, 9

        self.assertEqual(_intervals_intersection(a1, b1, a2, b2), 7)

    def test_intervals_intersection_no_intersection(self):
        a1, b1, a2, b2 = 0, 1, 2, 3

        self.assertEqual(_intervals_intersection(a1, b1, a2, b2), 0)


if __name__ == '__main__':
    unittest.main()
