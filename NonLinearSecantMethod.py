from math import *
def f(fx, q):
    x = q
    return eval(fx)

def findRootSM(fx,a,b,e):
    if f(fx, a) > 0:
        aIsPositive = True
    else:
        aIsPositive = False
    ef = b - a
    while ef > e:
        y1 = f(fx, a)
        y2 = f(fx, b)
        x = -y1/(y2-y1)*(b - a) + a
        if f(fx, x) == 0:
            return x
        if (aIsPositive and f(fx, x) < 0) or (not aIsPositive and f(fx, x) > 0):
            b = x
        else:
            ef = abs(a - x)
            a = x
    return x

print(findRootSM("-pow(x,2)+2",1,2,0.0001))