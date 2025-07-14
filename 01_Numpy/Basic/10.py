import numpy as np

a1 = np.arange(0, 12).reshape(3, 4)
a2 = np.arange(12, 24).reshape(3, 4)

print("Horizontal Stacking:")
print(np.hstack((a1, a2)))

print("Column Stack:")
print(np.column_stack((a1, a2)))

print("Concatenation along axis 1:")
print(np.concatenate((a1, a2), axis=1))

print("Vertical Stacking:")
print(np.vstack((a1, a2)))

print("Row Stack:")
print(np.row_stack((a1, a2)))

print("Concatenation along axis 0:")
print(np.concatenate((a1, a2), axis=0))

print("Stacking with new axis:")
print(np.stack((a1, a2), axis=0))

print("Stacking with new axis at 1:")
print(np.stack((a1, a2), axis=1))

print("Stacking with new axis at 2:")
print(np.stack((a1, a2), axis=2))

print("Depth Stacking:")
print(np.dstack((a1, a2)))

print("Reshape a1 to (2, 6):")
print(a1.reshape(2, 6)) 