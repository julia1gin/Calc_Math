from const import left_rectangle_h

def double_int(fx, a, b, ez):
    h = (b-a)/1000
    n = 0
    ans1 = left_rectangle_h(fx, a, b, h)
    n = n + int((b - a)/h)
    h = h/2
    ans2 = left_rectangle_h(fx, a, b, h)
    n = n + int((b - a) / h)
    while abs(ans2-ans1) > ez:
        ans1 = ans2
        h = h/2
        ans2 = left_rectangle_h(fx, a, b, h)
        n = n + int((b - a) / h)
    print(ans2)
    return ans2


def double_int_fixed(fx, a, b, ez):
    hv = (b-a)/1000
    n = 0
    hs = hv/2
    parity = True
    ans1 = left_rectangle_h(fx, a, b, hv)
    n = n + int((b - a) / hv)
    ans2 = left_rectangle_h(fx, a+hs, b, hv)
    ans2 = (ans2 + ans1)/2
    n = n + int((b - a - hs) / hv)
    while abs(ans2 - ans1) > ez:
        if parity:
            hv = hv / 2
        parity = not parity
        hs = hs/2
        ans1 = ans2
        q = ans1
        ans2 = (left_rectangle_h(fx, a+hs, b, hv) + q)/2
        n = n + int((b - a - hs)/hv)
    print(ans2)
    return ans2

