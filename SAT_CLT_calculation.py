# simple calculation using the CLT theorem
import numpy as np

p = 1/6 # probability
n = 40 # number of cases

var = 200/36
# var = n*p*(1-p) # variance

mu = 25/6
# mu = n*p # expectation

rho = np.sqrt(var) # standard deviation
a = 400 # set number from P(Sn >= a) = b
Zn = (a - n*mu)/(np.sqrt(n)*rho)

print("last line")
