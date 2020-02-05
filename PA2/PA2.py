import math


def function1(x: float):
    """
    Question 19
    :param x:
    :return:
    """
    return x - math.tan(x)


def function2(x: float):
    """
    Question 20
    :param x:
    :return:
    """
    return x ** 8 - 36 * x ** 7 + 546 * x ** 6 - 4536 * x ** 5 + 22449 * x ** 4 - 67284 * x ** 3 + \
           118124 * x ** 2 - 109584 * x + 40320


def function2a(x: float):
    """
    Question 20 repeating with 36.001
    :param x:
    :return:
    """
    return x ** 8 - 36.001 * x ** 7 + 546 * x ** 6 - 4536 * x ** 5 + 22449 * x ** 4 - 67284 * x ** 3 + \
           118124 * x ** 2 - 109584 * x + 40320


def sign(x: float):
    """
    Returns sign of a number
    :param x: The number
    :return: 1 if positive, -1 if negative
    """
    return (x > 0) - (x < 0)


def bisection(func):
    """
    The bisection algorithm
    :param func: The math function
    :return:
    """
    a = float(input("Input a"))
    b = float(input("Input b"))
    M = int(input("Input M"))
    delta = float(input("Input delta"))
    epsilon = float(input("Input epsilon"))
    u = func(a)
    v = func(b)
    e = b - a
    print("a = " + str(a))
    print("b = " + str(b))
    print("u = " + str(u))
    print("v = " + str(v))
    print()
    if sign(u) == sign(v):
        return
    for k in range(1, M - 1):
        e = e / 2
        c = a + e
        w = func(c)
        print("k = " + str(k))
        print("c = " + str(c))
        print("w = " + str(w))
        print("e = " + str(e))
        print()
        if abs(e) < delta or abs(w) < epsilon:
            return
        if sign(w) != sign(u):
            b = c
            v = w
        else:
            a = c
            u = w


if __name__ == '__main__':
    bisection(function1)
    bisection(function2)
    bisection(function2a)
