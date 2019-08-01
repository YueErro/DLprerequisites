import os
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import argparse

def parseArguments():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--rotateMode', help='numpy or for loop mode', type=str, choices=['numpy', 'for'], default='numpy')
    args = parser.parse_args()
    return args

def numpyRotation(pImg):
    return np.rot90(pImg, 3) # 90 degrees clockwise

def forRotation(pImg):
    rows, columns = pImg.shape
    rotImg = np.zeros((columns, rows))

    for i in range(rows):
        for j in range(columns):
            rotImg[j, rows-i-1] = pImg[i,j]

    return rotImg

def main(pArgs):
    ex4dir = os.path.dirname(os.path.realpath(__file__))
    parentPath = os.path.dirname(ex4dir)

    try:
        data = pd.read_csv(parentPath + '/data/train.csv')
    except IOError:
        raise Exception("File does not exist")

    dValues = data.values
    imgs = dValues[:, 1:]

    randomImg = random.randrange(imgs.shape[0])
    img = imgs[randomImg].reshape(28, 28)

    if pArgs.rotateMode == 'numpy':
        img = numpyRotation(img)
    elif pArgs.rotateMode == 'for':
        img = forRotation(img)

    plt.imshow(255-img, cmap='gray')
    plt.show()

if __name__ == '__main__':
    args = parseArguments()
    main(args)
