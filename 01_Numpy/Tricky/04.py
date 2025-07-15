import numpy as np

a1= np.random.randint(1,101,24)
a2= np.random.randint(1,101,24).reshape(6,4)

print(a1)
print(a2)

# items = [10,20,30,40,50,60,70,80,90,100]

# print(t1:=np.isin(a1,items))
# print(t2:=np.isin(a2,items))

# print(a1[t1])
# print(a2[t2])

# print(np.flip(a1))
# print(np.flip(a2))
# print(np.flip(a2),axis=0)
# print(np.flip(a2),axis=1)

# np.put(a1,[0,1], [11,12])
# np.put(a2,[0,1], [11,12])
# print(a1)
# print(a2)

print(np.delete(a1,[0,2,4]))