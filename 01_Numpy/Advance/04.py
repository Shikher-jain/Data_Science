import numpy as np


def sigmoid(array):
    return 1/(1 + np.exp(-(array)))

# Function to calculate Mean Squared Error
def mse(actual,predicted):
    return np.mean((actual - predicted) ** 2)

# Binary Cross Entropy
def binary_cross_entropy(actual, predicted):
    epsilon = 1e-15  # To avoid log(0)
    predicted = np.clip(predicted, epsilon, 1 - epsilon)  # Clip values to avoid log(0)
    return -np.mean(actual * np.log(predicted) + (1 - actual) * np.log(1 - predicted))

a1= np.arange(10)
print("Sigmoid of a1:",sigmoid(a1))

actual =np.random.randint(1,20,10)
predicted =np.random.randint(1,20,10)
print(actual)
print(predicted)
print("MSE of a1:",mse(actual,predicted))

print("Binary Cross Entropy of a1:",binary_cross_entropy(actual,predicted))         