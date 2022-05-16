import unittest
from app.subject import Subject, MIN_VALUE, MAX_VALUE, subjects_intersection, Intersection, _intervals_intersection


class TestSubjectClass(unittest.TestCase):
    """test ..app.subject.Subject"""

    def test_From1To6_setter(self):
        with self.assertRaises(ValueError):
            Subject(MIN_VALUE - 1, MIN_VALUE - 2, MAX_VALUE + 3)

    def test_attrs_order_all_equal(self):
        val = 3

        self.assertEqual(Subject(val, val, val).attrs_order(), "kpl")

    def test_attrs_order_k_max(self):
        k, p, l = 5.5, 4, 3

        self.assertEqual(Subject(k, p, l).attrs_order(), "kpl")

    def test_attrs_order_k_p_max(self):
        k, p, l = 6, 6, 4

        self.assertEqual(Subject(k, p, l).attrs_order(), "kpl")

    def test_attrs_order_k_l_max(self):
        k, p, l = 6, 3, 6

        self.assertEqual(Subject(k, p, l).attrs_order(), "kpl")

    def test_attrs_order_p_max(self):
        k, p, l = 3, 6, 4

        self.assertEqual(Subject(k, p, l).attrs_order(), "plk")

    def test_attrs_order_p_max(self):
        k, p, l = 3, 6, 4

        self.assertEqual(Subject(k, p, l).attrs_order(), "plk")

    def test_attrs_order_p_max(self):
        k, p, l = 3, 6, 6

        self.assertEqual(Subject(k, p, l).attrs_order(), "plk")

    def test_attrs_order_l_max(self):
        k, p, l = 3, 2, 5

        self.assertEqual(Subject(k, p, l).attrs_order(), "lkp")

    def test_lower_bounds(self):
        k, p, l = 3, 2, 1

        subject = Subject(k, p, l)

        self.assertEqual(subject.get_bounds(lower=True), Subject(1.5, 1.33, 1))

    def test_upper_bounds(self):
        k, p, l = 3, 2, 1

        subject = Subject(k, p, l)

        self.assertEqual(subject.get_bounds(lower=False), Subject(4.5, 2.67, 1.67))

    def test_lower_bounds_1(self):
        k, p, l = 3, 4, 2

        subject = Subject(k, p, l)

        self.assertEqual(subject.get_bounds(lower=True), Subject(1, 2, 1.33))

    def test_upper_bounds_1(self):
        k, p, l = 3, 4, 2

        subject = Subject(k, p, l)

        self.assertEqual(subject.get_bounds(lower=False), Subject(5, 6, 2.67))

    def test_subjects_intersection_zero(self):
        subject_1, subject_2 = Subject(1, 1, 1), Subject(6, 6, 6)

        self.assertEqual(subjects_intersection(subject_1, subject_2), Intersection(0, 0, 0))

    def test_subjects_intersection_from_example(self):

        subject_1, subject_2 = Subject(3, 2, 1), Subject(3, 4, 2)
        #                      kpl               plk

        s1_lower, s1_upper = subject_1.get_bounds(lower=True), subject_1.get_bounds(lower=False)
        s2_lower, s2_upper = subject_2.get_bounds(lower=True), subject_2.get_bounds(lower=False)

        by_k = _intervals_intersection(s1_lower.k, s1_upper.k, s2_lower.k, s2_upper.k)
        by_p = _intervals_intersection(s1_lower.p, s1_upper.p, s2_lower.p, s2_upper.p)
        by_l = _intervals_intersection(s1_lower.l, s1_upper.l, s2_lower.l, s2_upper.l)

        self.assertEqual(subjects_intersection(subject_1, subject_2), Intersection(by_k, by_p, by_l))


if __name__ == '__main__':
    unittest.main()
