def derivative_at_point(func, x, h=1e-6):
    return (func(x + h) - func(x - h)) / (2 * h)


def second_derivative_at_point(func, x, h=1e-6):
    return (func(x + h) - 2 * func(x) + func(x - h)) / (h ** 2)