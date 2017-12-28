import numpy as np
from scipy.stats import uniform
import matplotlib.pyplot as plt

np.random.seed()
N = 10000
rv = uniform(loc=0.0, scale=1.0)

x = rv.rvs(size=N)
nbins = 50
plt.hist(x ,nbins, normed=True)

x = np.linspace(rv.ppf(0), rv.ppf(1), 100)
plt.plot(x, uniform.pdf(x), 'r-', lw=2, label='uniform pdf')

plt.show()
