import numpy as np
from scipy.stats import uniform
import matplotlib.pyplot as plt

np.random.seed()
N = 10000
loc = 0.0
scale = 1.0
x = uniform.rvs(loc=loc, scale=scale, size=N)
nbins = 50
plt.hist(x, nbins, normed=True)

x = np.linspace(uniform.ppf(0, loc=loc, scale=scale), uniform.ppf(1, loc=loc, scale=scale), 100)
plt.plot(x , uniform.pdf(x, loc=loc, scale=scale), 'r-' , lw=2, label='uniform pdf')

plt.show()
