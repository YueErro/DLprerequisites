import numpy as np
import matplotlib.pyplot as plt

def getCoordinates(pData, pRadius):
    x = pRadius * np.sin(pData)
    y = pRadius * np.cos(pData)
    return x, y

def main():
    N = 800
    innerR = 20
    outerR = 40

    data = np.random.random(N) * 2 * np.pi
    noise = np.random.normal(0, 1.5, N)

    innerDonut = np.array(getCoordinates(data, innerR + noise))
    outerDonut = np.array(getCoordinates(data, outerR + noise))

    # Concatenate horizontally
    donuts = np.concatenate((innerDonut, outerDonut), axis=1)
    colors = np.append( np.full(N, "darkblue"), np.full(N, "darkred") )

    plt.scatter(donuts[0,:], donuts[1,:], c=colors, alpha=0.4)
    plt.show()

if __name__ == '__main__':
    main()
