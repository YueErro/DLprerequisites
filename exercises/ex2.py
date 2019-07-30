import numpy as np
import matplotlib.pyplot as plt

numSamples = 1000
Ys = np.zeros(numSamples)

for x in range(numSamples):
    X = np.random.uniform(size=numSamples)
    Y = X.sum()
    Ys[x] = Y

Ymean = np.mean(Ys)
Yvar = np.var(Ys)
plt.title('mean = ' + str( np.around(Ymean, 2) ) +
           ', variance = ' + str( np.around(Yvar, 2) ) )
plt.hist(Ys)
plt.show()
