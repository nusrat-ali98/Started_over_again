# some basic operations of numpy
import numpy as np

a = np.array([[7,8,9],[2,1,3],[3,2,1]])
print(a)

print(a.ndim)

b = np.array([[1,2,3,],[4,5,6,],[7,8,9]])
print(b)
print(b.ndim)

print(b.shape)

print(b.reshape(9,1))

c = np.arange(1,9,2)
print(c)

d = np.linspace(1,2,10)
print(d)

print(a.max())
print(a.min())
print(a.sum())

print(b.sum(axis=1))
print(b.sum(axis=0))

print(np.sqrt(b))

print(a + b)
print(a - b)
print(a * b)
print(a / b)