import numpy as np
d1 = [1, 2, 3]

z = np.zeros((3, 4))  # Creates a 3x4 array filled with zeros
o = np.ones((2, 3))  # Creates a 2x3 array filled with ones
print("Zero",z)
print("One",o)  

print("Identity",np.eye(3,dtype=int))  # Creates a 3x3 identity matrix
print("Full",np.full((2, 3), 7))  # Creates a 2x3 array filled with the value 7
print("Random",np.random.rand(2, 3))  # Creates a 2x3 array filled with random values
print("Random",np.random.random((2, 3)))  # Creates a 2x3 array filled with random values