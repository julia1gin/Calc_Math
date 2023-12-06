
def f(fx, q, w):
    x = q
    y = w
    return eval(fx)

answer = {}
def Euler(fx, x0, b, y0,n):
    h = (b-x0)/n
    x = x0
    y = y0
    while (x <= b-h):
        answer[x] = y
        y += h * f(fx, x, y)
        x += h
    answer[x] = y
    return answer