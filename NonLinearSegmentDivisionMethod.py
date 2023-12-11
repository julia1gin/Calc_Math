def f(fx, q):
    x = q
    return eval(fx)

def SegmentDivision(fx, a, b, E):
    while abs(b - a) >= E:
        fa = fx(a)
        x = (a+b) / 2
        fx = fx(x)
        if fa * fx < 0:
            b = x
        else:
            a = x
    return a, b