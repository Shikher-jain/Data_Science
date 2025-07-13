import numpy as np
d1 = [1, 2, 3]

n1 = np.arange(10)  # Generates an array with values from 0 to 9
n2 = np.arange(5, 15)  # Generates an array with values from 5 to

print(n1)   
print(n2)

n3 = range(10)  # Generates a range object with values from 0 to 9 14
print(n3)

r = n1.reshape(5, 2)  # Reshapes n1 into a 5x2 array
print(r)
n1.repeat(3)  # Repeats each element in n1 three times