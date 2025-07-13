import numpy as np

a1 = np.arange(10)  # Generates an array with values from 0 to 9
a2 = np.arange(15,dtype=float).reshape(3, 5)  # Generates an array with values from 5 to 14
a3 = np.arange(8).reshape(2,2,2)  # Generates an array with values from 5 to 14 with a step of 2

print("No. of dimensions:")
print(a1.ndim)  # Prints the number of dimensions of a1
print(a2.ndim)  # Prints the number of dimensions of a2
print(a3.ndim)  # Prints the number of dimensions of a3

print("Shape:") 
print(a1.shape)  # Prints the shape of a1
print(a2.shape)  # Prints the shape of a2
print(a3.shape)  # Prints the shape of a3

print("Size:")  
print(a1.size)  # Prints the size of a1
print(a2.size)  # Prints the size of a2
print(a3.size)  # Prints the size of a3

print("Data type:")
print(a1.dtype)  # Prints the data type of a1
print(a2.dtype)  # Prints the data type of a2
print(a3.dtype)  # Prints the data type of a3

print("Item size:")
print(a1.itemsize)  # Prints the size of each item in bytes for a1
print(a2.itemsize)  # Prints the size of each item in bytes for a2
print(a3.itemsize)  # Prints the size of each item in bytes for a3

print("Total bytes:")
print(a1.nbytes)  # Prints the total number of bytes used by a1
print(a2.nbytes)  # Prints the total number of bytes used by a2
print(a3.nbytes)  # Prints the total number of bytes used by a3

print("Transposed:")
print(a1)
print(a1.T)  # Transposes a1 (though it has no effect since it's 1D)
print(a2)
print(a2.T)  # Transposes a2
print(a3)
print(a3.T)  # Transposes a3

print("Flattened:")
print(a1.flatten())  # Flattens a1
print(a2.flatten())  # Flattens a2
print(a3.flatten())  # Flattens a3

print("Data type Before:")
print(a1.dtype)  # Prints the data type of a1
print(a2.dtype)  # Prints the data type of a2
print(a3.dtype)  # Prints the data type of a3

print("changing data type:")
print(a1.astype(float))  # Changes the data type of a1 to float
print(a2.astype(np.int16))    # Changes the data type of a2 to int
print(a3.astype(np.float64))  # Changes the data type of a3 to float64
print(a3.astype(np.str_))  # Changes the data type of a3 to string
