## SAT score question in U1 L2

from scipy.stats import bernoulli
from random import choices
from numpy import mean
import matplotlib.pyplot as plt

# parameters
a = 25 # success + |penalty|
b = -5 # penalty of failure
p = 3/6 # probability of success
size = 1000 # number of elements in the Bernoulli vector X
k = 40 # number of questions

# Bernoulli vector
X = bernoulli(p).rvs(size)

# Sum of scores
S = a*X + b

# get 1000 means (draw samples with replacement to preserve iid)
means = [mean((choices(S,k=k))) for i in range(100)]

# plot hist
plt.hist(means, bins=10)
#plt.xlim(0,1,0.1)
# plt.title()
plt.show()

print("finish")