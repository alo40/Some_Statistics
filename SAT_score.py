## SAT score question in U1 L2

from scipy.stats import bernoulli
from random import choices
from numpy import mean
import matplotlib.pyplot as plt

a = 25
b = -5
p = 1/6
size = 40
X = bernoulli(p).rvs(size)
S = a*X + b
print("finish")