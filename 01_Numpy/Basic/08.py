import numpy as np  


a1 = np.arange(1,28)
a2 = np.arange(1,29).reshape(7,4)
a3 = np.arange(0,27).reshape(3,3,3)

print(a1[5])

print(a2[5][2])
print(a2[5,2])

print(a3[2,2,2])
print(a3[2][2][2])

# ---------------------------------------------


print(a1)
print(a1[3:8])
print(a1[3:9:2])

print(a2)

print(a2[:4])
print(a2[:,3]) #col 3
print(a2[4,:]) # row 4
print(a2[1:5, 1:3]) # rows 1-5 and cols 1-3
print(a2[::6, ::3]) # corners
print(a2[::6, 1::2]) # 2 4 26 28
print(a2[3::5, ::3]) # 13 16
print(a2[3, ::3]) # 13 16

print(a3)

print(a3[1])
print(a3[::2])
print(a3[0,1])
print(a3[1,:,1]) # 10 13 16
print(a3[1][:,1]) # 10 13 16
print(a3[:,:,1]) # middle layer, all column
print(a3[:,0,::2]) # top corner layer, all column
print(a3[:,0::1,::2]) # bottom corner, all
print(a3[::2, 0::3, ::2]) # 0 2 18 20
print(a3[::2,0,::2]) # 0 2 18 20