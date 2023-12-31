
def f(fx, q, w):
    x = q
    y = w
    return eval(fx)


def runge_Kutta(fx, a, b, y0, h):
    y = y0
    x = a
    ans = {}
    while x < b:
        ans[x] = y
        k1 = h * f(fx, x, y)
        k2 = h * f(fx, x + h / 2, y + k1 / 2)
        k3 = h * f(fx, x + h / 2, y + k2 / 2)
        k4 = h * f(fx, x + h, y + k3)
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x += h
    return ans

