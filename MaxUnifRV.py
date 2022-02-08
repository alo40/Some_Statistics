import numpy as np
import matplotlib.pyplot as plt

def f(x, n):
    return n*(1-x**n)

x = np.linspace ( 0., 1, 101)
y = f(x, 2)
plt.plot(x, y)
plt.show()