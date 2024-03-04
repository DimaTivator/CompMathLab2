import math


def f1(x):
    return 2 * x ** 3 + 4 * x ** 2 - 5 * x + 7


def phi1(x):
    return math.sqrt(-0.25 * (2 * x ** 3 - 5 * x - 8))


def f2(x):
    return math.sin(4 * x ** 2 + 5) + 5 * x - 1


def phi2(x):
    return -0.2 * math.cos(4 * x ** 2 + 5) * 8 * x


def f3(x):
    return math.log(math.sqrt(x) + 4) + x ** 4 - 5 * x ** 3


def phi3(x):
    return (0.2 * (math.log(math.sqrt(x) + 4) + x ** 4)) ** (1 / 3)


