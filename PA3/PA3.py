import math


def newtonsAlgorithm(func, funcder):
    """
    Newtons method
    :param func: Equation
    :param funcder: Derivative of the equation
    :return:
    """
    x0 = float(input('x0'))
    m = int(input('M'))
    delta = float(input('delta'))
    epsilon = float(input('epsilon'))
    v = func(x0)
    print('k = 0')
    print('x0 = ' + str(x0))
    print('v = ' + str(v))
    if abs(v) < epsilon:
        return
    for k in range(1, m+1):
        x1 = x0 - v / funcder(x0)
        v = func(x1)
        print('k = ' + str(k))
        print('x1 = ' + str(x1))
        print('v = ' + str(v))
        if abs(x1 - x0) < delta or abs(v) < epsilon:
            return
        x0 = x1


def function1(x: float):
    return x - math.tan(x)


def function1der(x: float):
    return 1 - 1 / (math.cos(x)) ** 2


if __name__ == '__main__':
    newtonsAlgorithm(function1, function1der)