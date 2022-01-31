## SAT score question in U1 L2

from scipy.stats import bernoulli
from random import choices
from numpy import mean
import matplotlib.pyplot as plt

# parameters
a = 25 # success + |penalty|
b = -5 # penalty of failure
p = 1/6 # probability of success
size = 10000 # number of elements in the Bernoulli vector X (also total population size)
k = 40 # number of questions (elements extracted from the population size)
n = 1000 # number of iterations in the mean sample algorithm

# Bernoulli vector
X = bernoulli(p).rvs(size)

# Sum of scores
S = a*X + b
# S_bar = sum(S)

# # get 1000 means (draw samples with replacement to preserve iid)
# C = choices(S,k=k)
# M = sum(C)
means = [sum(choices(S,k=k)) for i in range(n)]

# plot hist
plt.hist(means, bins="auto")
plt.xlim(-200,800,50)
plt.title("%d samples of size %d from a population of %d (with p = %.2f)" % (n, k, size, p))
plt.show()

print("finish")