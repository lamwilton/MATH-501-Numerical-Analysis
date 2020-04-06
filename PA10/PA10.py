import numpy as np


def f(x: float):
    return 1 / (1 + 6 * x ** 2)


def getY(func):
    x = np.arange(-1, 1.001, 0.1)  # check n = 20
    return x, func(x)


def cubicSpline(t, y):
    n = np.size(y) - 1
    h, b, u, v = np.zeros(n), np.zeros(n), np.zeros(n), np.zeros(n)
    z = np.zeros(n+1)
    for i in range(0, n):
        h[i] = t[i + 1] - t[i]
        b[i] = 6 * (y[i + 1] - y[i]) / h[i]
    u[1] = 2 * (h[0] + h[1])
    v[1] = b[1] - b[0]
    for i in range(2, n):
        u[i] = 2 * (h[i] + h[i - 1]) - h[i - 1] ** 2 / u[i - 1]
        v[i] = b[i] - b[i - 1] - h[i - 1] * v[i - 1] / u[i - 1]
    for i in reversed(range(1, n)):
        z[i] = (v[i] - h[i] * z[i + 1]) / u[i]
    return z, h


def getEquation(z, h, y):
    A, C = np.zeros(np.size(y) - 1), np.zeros(np.size(y) - 1)
    for i in range(0, np.size(y) - 1):
        A[i] = 1 / (6 * h[i]) * (z[i + 1] - z[i])
        C[i] = - h[i] / 6 * z[i + 1] - h[i] / 3 * z[i] + 1 / h[i] * (y[i + 1] - y[i])
    B = z / 2
    return A, B, C


def splineFunction(x, A, B, C, y, t, i):
    return y[i] + (x - t[i]) * (C[i] + (x - t[i]) * (B[i] + (x - t[i]) * A[i]))


def evaluate(A, B, C, y, t):
    x = np.arange(-1, 1.001, 0.05)  # Check
    i = (x + 1) // 0.101  # Check
    i = i.astype(int)
    result, realresult = np.zeros(np.size(x)), np.zeros(np.size(x))
    for j in range(0, np.size(x)):
        result[j] = splineFunction(x[j], A, B, C, y, t, i[j])
        realresult[j] = f(x[j])
    return result, realresult, abs(result - realresult)


def main():
    x, y = getY(f)
    z, h = cubicSpline(t=x, y=y)
    A, B, C = getEquation(z, h, y)
    result, realresult, diff = evaluate(A, B, C, y, t=x)
    print("f(x)")
    print(realresult)
    print()
    print("p(x)")
    print(result)
    print()
    print("f(x) - p(x)")
    print(diff)


if __name__ == '__main__':
    main()