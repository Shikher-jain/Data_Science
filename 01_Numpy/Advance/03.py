from cv2 import AGAST_FEATURE_DETECTOR_AGAST_7_12S
import numpy as np

print("Broadcasting with Numpy Arrays")

# a1 = np.arange(4)
# a2 = np.arange(24).reshape(6,4)
# print(a1 + a2)  # Broadcasting: a1 is added to each row of a2

# error
# a1 = np.arange(4).reshape(4,)
# a2 = np.arange(64).reshape(4,16)
# print(a1 + a2)  # Broadcasting: a1 is added to a2

# a1 = np.arange(4).reshape(4,)
# a2 = np.arange(64).reshape(16,4)
# print(a1 + a2)  # Broadcasting: a1 is added to a2

# error
# a1 = np.arange(4).reshape(2,2)       
# a2 = np.arange(16).reshape(4,4)
# print(a1 + a2)  # Broadcasting: a1 is added to each row of a2

# a1 = np.arange(12).reshape(3,4)
# a2 = np.arange(12).reshape(4,3)
# print(a1 + a2)  # Broadcasting: a1 is added to each row of a2

# a1 = np.arange(1)
# a2 = np.arange(4).reshape(2,2)
# print(a1 + a2)  # Broadcasting: a1 is added to each row of a2

# error
# a1 = np.arange(3)
# a2 = np.arange(12).reshape(3,4)
# print(a1 + a2)  # Broadcasting: a1 is added to each row of a2

# a1 = np.arange(3).reshape(1,3)
# a2 = np.arange(4).reshape(4,1)
# print(a1 + a2)  # Broadcasting: a1 is added to each row of a2

# a1 = np.arange(4)
# a2 = np.arange(12).reshape(3,4)
# print(a1 + a2)  # Broadcasting: a1 is added to each row of a2

# error
# a1 = np.arange(4)
# a2 = np.arange(12).reshape(4,3)
# print(a1 + a2)  # Broadcasting: a1 is added to each row of a2

# a1 = np.arange(4)
# a2 = np.arange(24).reshape(6,4)
# print(a1 + a2)  # Broadcasting: a1 is added to each row of a2

# a1 = np.arange(4)
# a2 = np.arange(24).reshape(6,4)
# print(a1 + a2)  # Broadcasting: a1 is added to each row of a2

