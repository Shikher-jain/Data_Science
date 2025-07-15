import numpy as np
import time
import sys

a = [i for i in range(1000000)]
b = [i for i in range(1000000,2000000)]

print("Size of List a:", sys.getsizeof(a))
print("Size of List b:", sys.getsizeof(b))

c = []

start = time.time()
for i in range(1000000):
    c.append(a[i] + b[i])
end = time.time()
print("Time taken By Python List:", end - start)           

a1 = np.arange(1000000)
b1 = np.arange(1000000,2000000)

print("Size of NumPy Array a1:", sys.getsizeof(a1))
print("Size of NumPy Array b1:", sys.getsizeof(b1))
print("Size of NumPy Array a1:", a1.nbytes)
print("Size of NumPy Array b1:", b1.nbytes)

start1 = time.time()
c1 = a1 + b1
end1 = time.time()
print("Time taken By NumPy Array:", end1 - start1)

print((end - start) / (end1 - start1) ,  "Times")