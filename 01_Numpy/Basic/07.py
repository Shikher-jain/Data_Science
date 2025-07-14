import numpy as np

a1 = np.random.random((3, 4)) 
print(a1)
a1 = np.round(a1*100)
print(np.round(a1*100))  # Round to 2 decimal places
print(np.floor(a1*100))  # Round to 2 decimal places
print(np.ceil(a1*100))  # Round to 2 decimal places
print(a1)

# 0-> cols # 1-> rows

print("MAX")
print(np.max(a1))
print(np.max(a1,axis=0))
print(np.max(a1,axis=1))

print("MIN")
print(np.min(a1))
print(np.min(a1,axis=0))
print(np.min(a1,axis=1))

print("PRODUCT")
print(np.prod(a1))
print(np.prod(a1,axis=0))
print(np.prod(a1,axis=1))

print("SUM")
print(np.sum(a1))
print(np.sum(a1,axis=0))
print(np.sum(a1,axis=1))

print("SUM SQUARES")
print(np.mean(a1))
print(np.mean(a1, axis=0))
print(np.mean(a1, axis=1))

print("MEDIAN")
print(np.median(a1))
print(np.median(a1, axis=0))
print(np.median(a1, axis=1))

print("STANDARD DEVIATION")
print(np.std(a1))
print(np.std(a1, axis=0))
print(np.std(a1, axis=1))

print("VARIANCE")
print(np.var(a1))
print(np.var(a1, axis=0))
print(np.var(a1, axis=1))

print("TRIGONOMETRIC FUNCTIONS")
print(np.sin(a1))
print(np.arcsin(a1))
print(np.sinh(a1))

print(np.cos(a1))
print(np.arccos(a1))
print(np.cosh(a1))

print(np.tan(a1))
print(np.arctan(a1))
print(np.tanh(a1))

print("DOT PRODUCT")
print(np.dot(a1, a1.T))  # Dot product with its transpose
print(np.dot(a1.T, a1))  # Dot product with its transpose

print("DOT PRODUCT with different shapes")

a2=np.arange(12).reshape(3, 4)
a3=np.arange(12, 24).reshape(4, 3)
print(a2)
print(a3)

print(np.dot(a2, a3))  # Dot product with different shapes

print("LOGARITHM")
print(np.log(a1))
print(np.log10(a1))
print(np.log2(a1))
