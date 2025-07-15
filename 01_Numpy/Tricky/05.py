
import numpy as np

a1= np.random.randint(1,101,24)
a2= np.random.randint(1,101,24).reshape(6,4)

print(a1)
# print(a2)

# print(np.union1d(a1,a2))
# print(np.intersect1d(a1,a2))
# print(np.setdiff1d(a1,a2))
# print(np.setxor1d(a1,a2))

# print(np.in1d(a1,73))
# print(np.in1d(a1,33))
# print(np.in1d(a1,22))

# print(a1[np.in1d(a1,73)])
# print(a1[np.in1d(a1,33)])
# print(a1[np.in1d(a1,22)])

print(np.clip(a1,25,75))
