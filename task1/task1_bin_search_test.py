from compmath.nonlinear import *
import pandas as pd


def f(x):
    return -1.38 * x ** 3 - 5.42 * x ** 2 + 2.57 * x + 10.95


a = bin_search(f, -2, 0, 1e-2)
print(pd.DataFrame({
    'a': [x[0] for x in a],
    'b': [x[1] for x in a],
    'x': [x[2] for x in a],
    'f(a)': [x[3] for x in a],
    'f(b)': [x[4] for x in a],
    'f(x)': [x[5] for x in a],
    '|a - b|': [x[6] for x in a],
}))
