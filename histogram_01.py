## first example of histograms

from scipy.stats import bernoulli
from random import choices
from numpy import mean
import matplotlib.pyplot as plt

# freeze the population
k = 50 # number of couples drawn from total population (per sample taken)
p = 0.1 # probability of success
size = 5000 # total population size
total_samples = 1000 # number of total samples (per experiment)
population = bernoulli(p).rvs(size)

# get 1000 means (draw samples with replacement to preserve iid)
means = [mean((choices(population,k=k))) for i in range(total_samples)]

# take a look
plt.hist(means, bins=10)
plt.xlim(0,1,0.1)
# plt.title('1,000 samples of size 124 from a population of 5,000 (p=0.35)')
plt.show()