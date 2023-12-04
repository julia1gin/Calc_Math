def f(fx, q):
    x = q
    return eval(fx)

def findRootSM(fx,a,b,e):
    if f(fx, a) > 0:
        aIsPositive = True
    else:
        aIsPositive = False
    while b - a > e:
        
        if aIsPositive:
            ...