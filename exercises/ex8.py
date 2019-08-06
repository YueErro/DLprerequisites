import ex7
import numpy as np
import matplotlib.pyplot as plt

def getSpirals():
    N = 150

    # Formula of the arithmetic spiral
    rotation = 0.3
    distance = 6
    theta = np.random.random(N)
    r = rotation + distance * theta

    noise = np.random.normal(0, 0.2, 2 * N).reshape(2, N)

    # Negative theta to flip it
    spirals = np.asarray( ex7.getCoordinates(-theta, r) ) + noise
    colors = np.full(N, 'darkred')

    for i in range(1,6):
        spirals = np.concatenate( (spirals, np.asarray( ex7.getCoordinates(i-theta , r) ) + noise), axis=1 )

        if i % 2 == 0:
            colors = np.append(colors, np.full(N, 'darkred'))
        else:
            colors = np.append(colors, np.full(N, 'darkblue'))

    return spirals, colors

def main():
    spirals, colors = getSpirals()
    plt.scatter(spirals[0,:],spirals[1,:], c=colors, alpha = 0.4)
    plt.show()

if __name__ == '__main__':
    main()
