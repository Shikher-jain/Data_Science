import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(-10, 10, 100)

y=x
plt.plot(x, y)
plt.title("Linear Function")
plt.show()

y= np.sin(x)
plt.plot(x, y)
plt.title("Sine Function")
plt.show()

y= x**2
plt.plot(x, y)
plt.title("Quadratic Function")
plt.show()

y= x * np.log(x)
plt.plot(x, y)
plt.title("Logarithmic Function")
plt.show()

y= 1/(1+np.exp(-x))
plt.plot(x, y)
plt.title("Sigmoid Function")
plt.show()