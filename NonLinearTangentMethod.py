def f(func, q):
    x = q
    return eval(func)

def df(derivative, w):
    x = w
    return eval(derivative)


def method_tangent(func, derivative, a, b, E):
    if f(func, a) * df(derivative, a) > 0:
        x0 = a
    else:
        x0 = b
    x = x0
    x1 = x - f(func, x) / df(derivative, x)
    while abs(x1 - x) > E:
        x = x1
        x1 = x - f(func, x) / df(derivative, x)
    return x1