import numpy as np

a1= np.random.randint(1,101,24)
a2= np.random.randint(1,101,24).reshape(6,4)

# print(a1)
# print(a2)

# print(np.sort(a1))
# print(np.sort(a2,axis = 0))
# print(np.sort(a2,axis = 1))

# print(np.sort(np.sort(a2,axis = 0),axis = 1))
# print(np.sort(np.sort(a2,axis = 1),axis = 0))

# print(np.append(a1,[10,120]))


# print(np.append(a2, np.ones((a2.shape[0],1)),axis=1))
# print(np.append(a2, np.ones((a2.shape[0],2)),axis=1))

# print(np.append(a2, np.ones((a2.shape[1]))).reshape(a2.shape[0]+1,a2.shape[1]))
# print(np.append(a2, np.ones((a2.shape[1]))))

a3 = np.random.randint(1,6,12).reshape(3,4)
a4 = np.random.randint(5,10,12).reshape(3,4)

# print(a3)
# print(a4)
# print(np.concatenate((a3,a4)))
# print(np.concatenate((a3,a4),axis=1))

# print(np.unique(a4))
# print(np.unique(a3))

# print(np.expand_dims(a1,axis=1))
# print(np.expand_dims(a1,axis=0))

# print(np.where(a1>50))
# print(np.where(a2>50,1,0))

# print(np.where(a1>50,0,a1))
# print(np.where(a2>50,1,a2))

