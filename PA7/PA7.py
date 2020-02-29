import numpy as np


def luDecomposition(A):
    """
    LU decomposition
    :param A: Input matrix
    :return: Matrices L and U
    """
    n = np.size(A, 0)
    L = np.zeros([n, n])
    U = np.zeros([n, n])
    for k in range(0, n):
        L[k, k] = 1
        U[k, k] = (A[k, k] - np.dot(L[k, 0:k], U[0:k, k])) / L[k, k]
        for j in range(k, n):
            U[k, j] = (A[k, j] - np.dot(L[k, 0:k], U[0:k, j])) / L[k, k]
        for i in range(k, n):
            L[i, k] = (A[i, k] - np.dot(L[i, 0:k], U[0:k, k])) / U[k, k]
    return L, U


def inversePower(L, U, x, M):
    for k in range(0, M):
        y = np.dot(np.dot(np.linalg.inv(U), np.linalg.inv(L)), x)
        r = y[0]/x[0]
        x = y / np.max(abs(y))
        print("k = " + str(k + 1) + " x = " + str(x) + " r = " + str(r))


if __name__ == '__main__':
    A = np.array([[6, 5, -5], [2, 6, -2], [2, 5, -1]])
    x = np.array([3, 7, -13])
    L, U = luDecomposition(A)
    M = 25
    inversePower(L, U, x, M)
