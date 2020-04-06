import numpy as np


def f(x: float):
    """
    function
    :param x: input
    :return: output
    """
    return 1/(1 + 6 * x ** 2)


def initial(n, f):
    """
    Initialize x and c
    :param n: number of nodes
    :param f: function
    :return: x and c
    """
    c = np.zeros([n + 1, n + 1])
    x = np.arange(-1, 1.01, 0.1)
    c[:, 0] = f(x)
    return x, c


def divideddiff(x, c):
    """
    Divided difference algorithm
    :param x:
    :param c:
    :return: matrix c finished
    """
    n = np.size(x) - 1
    for j in range(1, n + 1):
        for i in range(0, n - j + 1):
            c[i, j] = (c[i + 1, j - 1] - c[i, j - 1]) / (x[i + j] - x[i])
    return c


def poly(inputx, x, c):
    """
    Newton interpolating polynomial
    :param inputx: input value x
    :param x: x from table
    :param c: c from table
    :return: result
    """
    n = np.size(x)
    p = 0
    result = 0
    for j in range(0, n):
        temp = c[0, j]
        for i in range(0, j):
            temp = temp * (inputx - x[i])
        result += temp
    return result


def main():
    """
    Testing method
    :return:
    """
    x, c = initial(n=20, f=f)
    c = divideddiff(x, c)
    print("=========== n = 20 ===========")

    xtest = np.arange(-1, 1.0001, 0.05)
    ytest = np.array(poly(xtest, x, c))
    ftest = np.array(f(xtest))
    print("f(x)")
    print(f(xtest))
    print()
    print("p(x)")
    print(ytest)
    print()
    print("f(x) - p_n(x) for 41 points: ")
    print(ftest - ytest)
    print()


if __name__ == '__main__':
    main()
