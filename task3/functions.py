import math


def f1(x):
    return 2 * x ** 3 + 4 * x ** 2 - 5 * x - 8


def phi1(x):
    return math.sqrt(-0.25 * (2 * x ** 3 - 5 * x - 8))


def f2(x):
    return math.sin(4 * x ** 2 + 5) + 5 * x - 1


def phi2(x):
    return -0.2 * (math.sin(4 * x ** 2 + 5) - 1)


def f3(x):
    return math.log(math.sqrt(x) + 4) + x ** 4 - 5 * x ** 3


def phi3(x):
    return (0.2 * (math.log(math.sqrt(x) + 4) + x ** 4)) ** (1 / 3)


def y_0(x):
    return 0


def sys_f11(x, y):
    return 0.1 * x ** 2 + x + 0.2 * y ** 2 - 0.3


def sys_phi11(x, y):
    return 0.3 - 0.1 * x ** 2 - 0.2 * y ** 2


def sys_f12(x, y):
    return 0.2 * x ** 2 + y + 0.1 * x * y - 0.7


def sys_phi12(x, y):
    return 0.7 - 0.2 * x ** 2 - 0.1 * x * y


def sys_f21(x, y):
    return math.log(x) + y - 4


def sys_phi21(x, y):
    return math.exp(4 - y)


def sys_f22(x, y):
    return 1.3 * y ** 2 - 0.3 * x * y - 10


def sys_phi22(x, y):
    return math.sqrt(1 / 1.3 * (0.3 * x * y + 10))

