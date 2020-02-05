import numpy as np


def newtonNonLinear(f, fdx, fdy):
    """
    Non-linear system newtons method
    :param f: List of equations
    :param fdx: List of partial derivative x of the equations
    :param fdy: List of partial derivative y of the equations
    :return:
    """
    # Input for vector x0
    x00 = float(input('x0'))
    x10 = float(input('y0'))
    x0 = np.array([x00, x10])

    m = int(input('M'))
    delta = float(input('delta'))
    epsilon = float(input('epsilon'))
    v = np.array([func(x0) for func in f])
    print('k = 0')
    print('x0 = ' + str(x0))
    print('v = ' + str(v))

    if abs(np.max(v)) < epsilon:
        return
    for k in range(1, m+1):
        J = np.array([[funcx(x0), funcy(x0)] for (funcx, funcy) in (fdx, fdy)]).T
        x1 = x0 - np.dot(np.linalg.inv(J), v)
        v = np.array([func(x1) for func in f])
        print('k = ' + str(k))
        print('x1 = ' + str(x1))
        print('v = ' + str(v))
        if abs(np.max(x1 - x0)) < delta or abs(np.max(v)) < epsilon:
            return
        x0 = x1


def f1(x):
    return 4 * x[1] ** 2 + 4 * x[1] + 52 * x[0] - 19


def f1dx(x):
    return 52


def f1dy(x):
    return 8 * x[1] + 4


def f2(x):
    return 169 * x[0] ** 2 + 3 * x[1] ** 2 + 111 * x[0] - 10 * x[1] - 10


def f2dx(x):
    return 338 * x[0] + 111


def f2dy(x):
    return 6 * x[1] - 10


if __name__ == '__main__':
    f = [f1, f2]
    fdx = [f1dx, f2dx]
    fdy = [f1dy, f2dy]
    newtonNonLinear(f, fdx, fdy)