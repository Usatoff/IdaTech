from app.subject import Subject, subjects_intersection
import pandas as pd

import random
from itertools import combinations

random.seed(42)


if __name__ == "__main__":

    subjects = [Subject(random.random() * 5 + 1, random.random() * 5 + 1, random.random() * 5 + 1)
                for i in range(5)]

    subjects_1, subjects_2 = [], []
    for i, j in combinations(subjects, 2):
        subjects_1.append(i)
        subjects_2.append(j)

    df = pd.DataFrame({"subject_1": subjects_1, "subject_2": subjects_2})

    df["lower_bounds_1"] = df.subject_1.map(lambda x: x.get_bounds(lower=True))
    df["upper_bounds_1"] = df.subject_1.map(lambda x: x.get_bounds(lower=False))
    df["lower_bounds_2"] = df.subject_2.map(lambda x: x.get_bounds(lower=True))
    df["upper_bounds_2"] = df.subject_2.map(lambda x: x.get_bounds(lower=False))

    df["order_1"] = df.subject_1.map(lambda x: x.attrs_order())
    df["order_2"] = df.subject_2.map(lambda x: x.attrs_order())

    df["intersection"] = df.apply(lambda line:
                                  subjects_intersection(line.subject_1, line.subject_2),
                                  axis=1)
    df = df[["lower_bounds_1", "subject_1", "upper_bounds_1", "order_1",
             "lower_bounds_2", "subject_2", "upper_bounds_2", "order_2",
             "intersection"]]

    print(df.to_string())
