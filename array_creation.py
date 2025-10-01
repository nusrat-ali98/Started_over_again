import numpy as np


"""creating 1D array"""
a = np.arange(10,21)

print(a)

"""creating 2D array"""
b = np.zeros((3,4))
print("\n", b)

"""creating 3D array
       generating random 3d array values from 1 to 100 """

c = np.random.randint(1,101, size=(2,3,4))
print("\n", c)

"""Identity matrix  5X5 """

d = np.identity(5,int)
print("\n", d)

""" Creating an array with values [1,2,3] and repeating them 4 times"""

e = np. tile((1,2,3),4).reshape(4,3)
print("\n", e)