import numpy as np

"""Creating two arrays"""

a = np.array([1,2,3,4,5])
b = np.array([5,7,8,9,0])

"""Adding two arrays"""
c = np.add(a,b)
print(c)

"""Multiplying two arrays  by elements"""
c = a * b
print(c)

"""Different syntax for multiplying two arrays"""
c = np.multiply(a,b)
print(c)

"""Dot product of two arrays"""
c = np.dot(a,b)
print(c)

""" DIvision of two arrays"""
c = b/a
print(c)