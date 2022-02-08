import numpy as np
import matplotlib.pyplot as plt

# X_n = max(X_1, ..., X_n) where X_n are iid Unif[a,b] with a=0, b=1

## pdf function
def pdf(x, n, a, b):
    return n*(x-a)**(n-b)/(b-a)**n # pdf of X_n

## cdf function
def cdf(x, n, a, b):
    return ((x-a)/(b-a))**n # CFD of X_n

## pdf of the limit function
def pdf_limit(x, n, a, b):
    return n*(1-n*(x-a)**(n-b)/(b-a)**n)

## parameters
a = 0 # lower limit of Unif. distribution
b = 1 # upper limit of Unif. distribution
n = 100 # Number of iid X
x = np.linspace ( 0., 1, 101)

## plot
y1 = pdf(x, n, a, b)
# y2 = cdf(x, n, a, b)
# y3 = pdf_limit(x, n, a, b)
plt.plot(x, y1, 'r') # pdf plot
# plt.plot(x, y2, 'b') # cdf plot
# plt.plot(x, y3, 'g') # pdf_limit plot
plt.show()

## Some not used verbatim
# return n*(1-x**n) # is the CFD of some other function --> not correct