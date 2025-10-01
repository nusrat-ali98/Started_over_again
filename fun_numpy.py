import numpy as np


""""Creating an array of size (4, 4) with random elements"""
a = np.random.randint(1,10,size=(4,4))
print(a,"\n")

"""Summing up whole array"""
sum = np.sum(a)
print(sum,"\n")

"""Finding maximum no in each row"""
for i in range(len(a)):
    row_max = np.max(a[i,:5])
    print(row_max)
print()

"""Finding maximum no in each column"""
for i in range(len(a)):
    col_max = np.max(a[:5,i])
    print(col_max)
