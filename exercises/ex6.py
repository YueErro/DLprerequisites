import numpy as np
import matplotlib.pyplot as plt

N = 1000
data = np.random.uniform(-1, 1,(N, 2))

C = np.zeros(N)
C[(data[:,0] < 0) & (data[:,1] > 0)] = 1
C[(data[:,0] > 0) & (data[:,1] < 0)] = 1

plt.scatter(data[:,0], data[:,1], c=C)
plt.show()
