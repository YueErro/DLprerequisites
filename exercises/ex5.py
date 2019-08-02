import random
import numpy as np

def makeMatSymmetric(pMatrix):
    return (pMatrix + pMatrix.T) / 2

def numpyCheckSymmetric(pMatrix):
    return np.array_equal(pMatrix, pMatrix.T)

def manualCheckSymmetric(pMatrix):
    rows, columns = pMatrix.shape

    for r in range(rows):
        for c in range(columns):
            if pMatrix[r, c] != pMatrix[c, r]:
                return False
    return True

def main(pMode):
    # 3x3 matrix with numbers [0, ..., 9]
    M = np.random.random_integers( 0, 9, size=(3,3) )

    makeSymmetric = random.choice([True, False])
    if makeSymmetric:
        M = makeMatSymmetric(M)

    print(M)

    if pMode == 'manual':
        isSymmetric = manualCheckSymmetric(M)
    else:
        isSymmetric = numpyCheckSymmetric(M)

    if isSymmetric:
        print("It is symmetric")
    else:
        print("It is not symmetric")

if __name__ == '__main__':
    mode = None

    while mode != 'manual' and mode != 'numpy':
        mode = input("Mode? [manual/numpy]:")

    main(mode)
