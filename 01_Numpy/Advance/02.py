import numpy as np

# print('Fancy Indexing with Numpy Arrays')

# a1= np.arange(24).reshape(6,4)
# print(a1)

# print("Rows : 0 4 3 5\n",a1[[0,4,3,5]])
# print("Cols : 0 2 3\n",a1[:,[0,2,3]])

print('Boolean Indexing with Numpy Arrays')

a2= np.random.randint(1,100,24).reshape(6,4)
print(a2)

print(np.where(a2>50))  # Returns indices where condition is True
print(np.where(a2>50,a2,0))  # Returns array with values where condition is True, else 0
print(a2[a2>50]) #greater than 50
print(a2[a2%2==0]) #even numbers                            

print((a2%2==0) & (a2>50))  # Boolean condition for even numbers greater than 50
print(a2[(a2%2==0) & (a2>50)])
print(a2[(a2%2==0) | (a2>50)])  # Boolean condition for even numbers or greater than 50