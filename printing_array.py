import numpy as np

""" Creating an array with numbers from 0 to 50 in steps of 5"""

a = np.arange(0, 51, 5)
print(a)

"""Printing first 3 elements"""
print(a[:3],"\n")

"""Printing last 2 elements"""
print(a[-2:],"\n")

"""Print every alternative elements"""
print(a[::2],"\n")


""""Creating 2D array of shape (4, 4)"""
b = np.arange(16).reshape(4,4)
print(b,"\n")


"""Printing the first row of an array 'b'"""
print(b[0,:4],"\n")

"""Printing first column of an array 'b'"""
print(b[:4,0],"\n")

"""Printing the element at row 2 and column 3 of an array 'b' """
print(b[1,2])