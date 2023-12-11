def f(fx, q):
    x = q
    return eval(fx)


def SegmentDivision(fx, a, b, E):
    while abs(b - a) >= E:
        fa = f(fx, a)
        m = (a + b) / 2
        fm = f(fx, m)
        if fa * fm < 0:
            b = m
        elif fm == 0:
            return m, m
        else:
            a = m
    return a, b