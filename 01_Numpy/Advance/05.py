import numpy as np

a1=np.array([1,2,3,4,np.nan,6,7,8,9,10 ])

print(a1)

print(np.isnan(a1))  # Check for NaN values
print(a1[np.isnan(a1)])  # Check for NaN values
print(~np.isnan(a1))  # Check for NaN values
print(a1[~np.isnan(a1)])  # Check for NaN values