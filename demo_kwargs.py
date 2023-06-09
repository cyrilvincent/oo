def add(*kargs, **kwargs ):
    for t in kargs:
        print(t)
    for key in kwargs.keys():
        print(key, kwargs[key])

add(1,2,3,4,5,6, toto="titi")

import numpy as np

a1 = np.array([1,2,3,4])
a2 = np.array([1,2,3,4])
res = np.dot(a1, a2)
res = a1.dot(a2)

import pandas as pd

dataframe = pd.read_csv("data/media/books.csv")
print(dataframe.describe())
print(dataframe["price"])
print(dataframe.price)





