import numpy as np

def print_array(arr):
    print("Array shape:", arr.shape)
    for i in arr:
        print(i, end=' ')
        print()

def print_array_iter(arr):
    print("Array shape:", arr.shape)
    for i in np.nditer(arr):
        print(i, end=' ')
    print()


a1 = np.arange(0, 28)
a2 = np.arange(0, 28).reshape(7, 4)
a3 = np.arange(0, 27).reshape(3, 3, 3)

# print_array(a1)
# print_array(a2)
# print_array(a3) 

# print_array_iter(a1)
# print_array_iter(a2)
# print_array_iter(a3)

print(np.transpose(a1))
print(np.transpose(a2))
print(np.transpose(a3))

print(a1.T)
print(a2.T)
print(a3.T)

print(a1.ravel())
print(a2.ravel())
print(a3.ravel())

print(a1.flatten())
print(a2.flatten())
print(a3.flatten())