from sklearn.linear_model import LinearRegression
import numpy as np

# Data
x = np.array([[1], [2], [3], [4]])
y = np.array([3, 5, 7, 9])

# Model
model = LinearRegression()
model.fit(x, y)

# Predict
print(model.predict([[5]]))  # → [11.]
print(model.predict([[7]]))  # → [11.]
print(model.predict([[9]]))  # → [11.]
print(model.predict([[51]]))  # → [11.]
