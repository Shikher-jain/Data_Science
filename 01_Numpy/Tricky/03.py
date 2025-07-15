import numpy as np

a1= np.random.randint(1,101,24)
a2= np.random.randint(1,101,24).reshape(6,4)

print(a1)
print(a2)

print(np.cumsum(a1))
print(np.cumsum(a2))
print(np.cumsum(a2,axis=0))
print(np.cumsum(a2,axis=1))

print(np.cumprod(a1))
print(np.cumprod(a2))
print(np.cumprod(a2,axis=0))
print(np.cumprod(a2,axis=1))

print(np.percentile(a1,50))
print(np.percentile(a1,15))

print(np.percentile(a2,50))
print(np.percentile(a2,15))

print(np.histogram(a1))
print(np.histogram(a2))

print(np.histogram(a1,bins=[0,10,20,30,40,50,60,70,80,90,100]))
print(np.histogram(a2,bins=[0,10,20,30,40,50,60,70,80,90,100]))

salary = np.array([200,400,250,350,600])
xp = np.array([1,3,2,4,2])
print(np.corrcoef(salary,xp))
