import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ex3dir = os.path.dirname(os.path.realpath(__file__))
parentPath = os.path.dirname(ex3dir)

try:
    data = pd.read_csv(parentPath + '/data/train.csv')
except IOError:
    raise Exception("File does not exist")

dValues = data.values
numDigits = 10
imgs = dValues[:, 1:]
labels = dValues[:, 0]

for x in range(numDigits):
    img = imgs[labels==x] # by digit
    img = np.mean(img, axis=0)

    img = img.reshape(28, 28)
    plt.imshow(255-img, cmap='gray')
    plt.show()
