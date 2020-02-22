import numpy as np


def main(A, b, x, M):
    """
    Gauss-Seiden Algorithm
    :param A: Matrix A such that Ax = b
    :param b: Vector b
    :param x: Starting guess of x
    :param M: Number of iterations
    :return:
    """
    n = np.size(A, 0)
    for k in range(0, M):
        x = (b - (np.dot(A, x) - np.multiply(np.diag(A), x))) / np.diag(A)
    print("k = " + str(k + 1))
    print("x = " + str(x))
    print("Checking Ax = b")
    print(str(np.dot(A, x)))


if __name__ == '__main__':
    A = np.array([[0.96326, 0.81321], [0.81321, 0.68654]])
    b = np.array([0.88824, 0.74988])
    x = np.array([0.33116, 0.7])
    M = 1000
    main(A, b, x, M)