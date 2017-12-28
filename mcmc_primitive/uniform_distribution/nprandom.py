import numpy as np
import matplotlib.pyplot as plt

np.random.seed()
N=10000
x = np.random.uniform(0.0, 1.0, N)
nbins=50
plt.hist(x, nbins, normed=True)
plt.show()
