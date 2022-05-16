from collections import namedtuple

MIN_VALUE, MAX_VALUE = 1., 6.

_move_in_range = lambda value: min(max(MIN_VALUE, value), MAX_VALUE)

# round only for test
_intervals_intersection = lambda a1, b1, a2, b2: round(max(min(b1, b2) - max(a1, a2), 0.), 1)


class From1To6:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not MIN_VALUE <= value <= MAX_VALUE:
            raise ValueError(f"value=0, but have to be {MIN_VALUE} <= value <= {MAX_VALUE}")
        # round only for test
        instance.__dict__[self.name] = round(value, 1)


class Subject:
    delta_muls = [1 / 2,
                  1 / 3,
                  2 / 3]

    k, p, l = From1To6(), From1To6(), From1To6()

    def __init__(self, k, p, l):
        self.k = k
        self.p = p
        self.l = l

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Subject) or not super().__eq__(o):
            return False

        try:
            return self.k == o.k and self.p == o.p and self.l == o.l
        except AttributeError:
            return False

    def __repr__(self) -> str:
        return "(" + ", ".join(f"{attr}=" + str(self.__dict__[attr]) for attr in "kpl") + ")"

    def attrs_order(self):
        if self.k >= self.l and self.k >= self.p:
            return "kpl"
        if self.p >= self.l:
            return "plk"
        return "lkp"

    def get_bounds(self, lower: bool):
        sign = -1 if lower else 1

        bounds = {}
        for position, attr_name in enumerate(self.attrs_order()):
            bounds[attr_name] = \
                _move_in_range(
                    self.__dict__[attr_name] + sign * Subject.delta_muls[position] * self.__dict__[attr_name]
                )
        return Subject(**bounds)


Intersection = namedtuple("Intersection", ["k", "p", "l"])


def subjects_intersection(s1: Subject, s2: Subject):
    s1_lower, s1_upper, s2_lower, s2_upper = s1.get_bounds(lower=True), s1.get_bounds(lower=False), \
                                             s2.get_bounds(lower=True), s2.get_bounds(lower=False)
    intersection_kwargs = {}
    for field in Intersection._fields:
        intersection_kwargs[field] = _intervals_intersection(s1_lower.__dict__[field],
                                                             s1_upper.__dict__[field],
                                                             s2_lower.__dict__[field],
                                                             s2_upper.__dict__[field])
    return Intersection(**intersection_kwargs)
