import numpy as np
import matplotlib.pyplot as plt

# Indicator of an exponential function
# X ~ exp(lambda) with lambda > 0
# Y = I(X>5)
# Statistical model: ({0,1}, {Ber(f(lambda))}_lambda>0)

## exponential distribution
def exponential(L, x):
    return L*np.exp(-L*x)

## parameters
L = 0.5 # lambda value (default)
x = np.linspace ( 0., 5, 101)

## plot
plt.plot(x, exponential(0, x), 'r')
plt.plot(x, exponential(0.5, x), 'b')
plt.plot(x, exponential(1, x), 'g')
plt.grid()
plt.show()

