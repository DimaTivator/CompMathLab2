from compmath.calc import *
from compmath.nonlinear import newton_method
import pandas as pd


def f(x):
    return -1.38 * x ** 3 - 5.42 * x ** 2 + 2.57 * x + 10.95


a = newton_method(f, -5, -3, 1e-2)
print(pd.DataFrame({
    'x_i': [x[0] for x in a],
    'f(x_i)': [x[1] for x in a],
    "f'(x_i)": [x[2] for x in a],
    'x_i+1': [x[3] for x in a],
    '|x_i+1 - x_i|': [x[4] for x in a],
}))

