def simple_iteration(phi, f, a, b, eps=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("Method is not applicable on this interval")

    x_prev = a
    log = []

    for _ in range(max_iter):
        x_new = phi(x_prev)
        print(x_prev, x_new, f(x_new), abs(x_new - x_prev))
        log.append((x_prev, x_new, phi(x_new), f(x_new), abs(x_new - x_prev)))

        if abs(x_new - x_prev) < eps:
            break

        x_prev = x_new

    if len(log) == max_iter:
        print("Reached maximum number of iterations!")

    return log


def chord_method(f, a, b, eps=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("Method is not applicable on this interval")

    x0 = a
    x1 = b
    log = []

    for _ in range(max_iter):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0 = x1
        x1 = x2
        log.append((x0, x1, x2, f(x0), f(x1), f(x2), x1 - x0))

        if abs(f(x1)) < eps:
            break

    if len(log) == max_iter:
        print("Reached maximum number of iterations!")

    return log


def bin_search(f, a, b, eps=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("Method is not applicable on this interval")

    log = []
    start = f(a)

    for _ in range(max_iter):
        m = (a + b) / 2
        if f(m) * start < 0:
            b = m
        else:
            a = m

        log.append((a, b, m, f(a), f(b), f(m), b - a))

        if abs(f(m)) < eps:
            break

    if len(log) == max_iter:
        print("Reached maximum number of iterations!")

    return log

