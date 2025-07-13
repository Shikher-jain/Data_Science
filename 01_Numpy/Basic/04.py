import numpy as np

l1 = np.linspace(0, 1, 5)  # Generates 5 evenly spaced values between 0 and 1
print("Linspace:", l1)

l2 = np.linspace(0, 1, 5, endpoint=False)  # Generates 5 evenly spaced values between 0 and 1, excluding the endpoint
print("Linspace:", l2)

l3, step = np.linspace(0, 1, 5, retstep=True)  # Generates 5 evenly spaced values between 0 and 1
print("Linspace:", l3)
print("Step size:", step)

l4, step = np.linspace(0, 1, 5, endpoint=True, retstep=True, dtype=float)  # Generates 5 evenly spaced values between 0 and 1, including the endpoint
print("Linspace:", l4)
print("Step size:", step)
print("Data type:", l4.dtype)

l5, step = np.linspace(0, 1, 5, endpoint=True, retstep=True, dtype=int)  # Generates 5 evenly spaced values between 0 and 1, including the endpoint
print("Linspace:", l5)
print("Step size:", step)
print("Data type:", l5.dtype)   
