import numpy as np
import matplotlib.pyplot as plt

A = np.array([
    [0.3, 0.6, 0.1],
    [0.5, 0.2, 0.3],
    [0.4, 0.1, 0.5]
])
v = np.ones(3) / 3
numTimes = 25
ed = np.zeros(numTimes)

for x in range(numTimes):
    aux = v.dot(A)
    euclideanDist = np.linalg.norm(aux-v)
    ed[x] = euclideanDist
    v = aux

plt.plot(ed)
plt.show()
