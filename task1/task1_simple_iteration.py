from compmath.nonlinear import *
import pandas as pd


def phi(x):
    return ((-1.38 * x ** 3 + 2.57 * x + 10.95) / 5.42) ** 0.5


def f(x):
    return -1.38 * x ** 3 - 5.42 * x ** 2 + 2.57 * x + 10.95


a = simple_iteration(phi, f, 1, 2, 1e-2)
print(pd.DataFrame({
    'x_k': [x[0] for x in a],
    'x_k+1': [x[1] for x in a],
    'phi(x_k+1)': [x[2] for x in a],
    'f(x_k+1)': [x[3] for x in a],
    '|x_k - x_k+1|': [x[4] for x in a],
}))
