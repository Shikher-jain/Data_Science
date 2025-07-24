import numpy as np

a = np.load('student.npy', allow_pickle=True)
print(a['name'])  

