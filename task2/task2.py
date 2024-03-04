import math
import pandas as pd
from compmath import cramer_2d


def f11(x, y):
    return y / (math.cos(x * y + 0.1) ** 2) - 2 * x


def f12(x, y):
    return x / (math.cos(x * y + 0.1) ** 2)


def F1(x, y):
    return x ** 2 - math.tan(x * y + 0.1)


def f21(x, y):
    return 2 * x


def f22(x, y):
    return 4 * y


def F2(x, y):
    return 1 - x ** 2 - 2 * y ** 2


x = -0.5
y = -0.5
dx = 1
dy = 1

eps = 0.01

log = []

while abs(dx) > eps and abs(dy) > eps:
    dx, dy = cramer_2d([
        [f11(x, y), f12(x, y)],
        [f21(x, y), f22(x, y)]
    ], [F1(x, y), F2(x, y)])

    x += dx
    y += dy

    log.append([x - dx, y - dy, x, y, dx, dy])

print(pd.DataFrame({
    'x': [x[0] for x in log],
    'y': [x[1] for x in log],
    'x + dx': [x[2] for x in log],
    'y + dy': [x[3] for x in log],
    'dx': [x[4] for x in log],
    'dy':  [x[5] for x in log]
}))





