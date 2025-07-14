import numpy as np

a1 = np.arange(0, 12).reshape(3, 4)
a2 = np.arange(12, 24).reshape(3, 4)

print("Horizontal Splitting:")
print(np.hsplit(a1, 2))
print(np.hsplit(a2, 2))

print("Vertical Splitting:")
print(np.vsplit(a1, 3))
print(np.vsplit(a2, 3))