from const import left_rectangle_h

def double_int(fx, a, b, ez):
    h = (b-a)/1000
    ans1 = left_rectangle_h(fx, a, b, h)
    h = h/2
    ans2 = left_rectangle_h(fx, a, b, h)
    while abs(ans2-ans1) > ez:
        ans1 = ans2
        h = h/2
        ans2 = left_rectangle_h(fx, a, b, h)
    print(ans2)
    return ans2


def double_int_fixed(fx, a, b, ez):
    hv = (b-a)/1000
    hs = hv/2
    parity = True
    ans1 = left_rectangle_h(fx, a, b, hv)
    ans2 = left_rectangle_h(fx, a+hs, b, hv)
    ans2 = (ans2 + ans1)/2
    while abs(ans2 - ans1) > ez:
        if parity:
            hv = hv / 2
        parity = not parity
        hs = hs/2
        ans1 = ans2
        q = ans1
        ans2 = (left_rectangle_h(fx, a+hs, b, hv) + q)/2
    print(ans2)
    return ans2