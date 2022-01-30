print("is working!")

from scipy.stats import bernoulli
from random import choices
from numpy import mean
import matplotlib.pyplot as plt

# freeze the population
population = bernoulli(p=0.35).rvs(size=5000)

# get 1000 means (draw samples with replacement to preserve iid)
means = [mean((choices(population,k=124))) for i in range(1000)]

# take a look
plt.hist(means, bins=10)
plt.title('1,000 samples of size 124 from a population of 5,000 (p=0.35)')
plt.show()