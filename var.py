from const import left_rectangle as right_rectangle

def double_int(fx, a, b, ez):
    h = ez**(1/2)
    n = int((b - a)/h)

    ans1 = right_rectangle(fx, a, b, n)
    n = n*2
    ans2 = right_rectangle(fx, a, b, n)
    while(abs(ans2-ans1) > ez):
        ans1 = ans2
        n = n*2
        ans2 = right_rectangle(fx, a, b, n)
    return ans2

def double_int_fixed(fx,a,b,ez):
    h = ez**(1/2)
    hv = h/2
    n = int((b-a)/h)
    parity = True
    ans1 = right_rectangle(fx, a, b, n)
    ans2 = (right_rectangle(fx, a+hv, b, n) + ans1) / 2
    while (abs(ans2 - ans1) > ez):
        hv = hv / 2
        q = ans1
        ans1 = ans2
        ans2 = (right_rectangle(fx, a+hv, b, n) + q)/2
        if parity:
            n = n*2
        parity = not parity
    return ans2