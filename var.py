from const import left_rectangle_h as right_rectangle


def double_int(fx, a, b, ez):
    h = ez**(1/2)

    ans1 = right_rectangle(fx, a, b, h)
    h = h/2
    ans2 = right_rectangle(fx, a, b, h)
    while abs(ans2-ans1) > ez:
        ans1 = ans2
        h = h/2
        ans2 = right_rectangle(fx, a, b, h)
    return ans2


def double_int_fixed(fx, a, b, ez):
    hv = ez**(1/2)
    hs = hv/2
    parity = True
    ans1 = right_rectangle(fx, a, b, hv)
    ans2 = (right_rectangle(fx, a+hs, b, hv) + ans1)/2
    while abs(ans2 - ans1) > ez:
        hs = hs/2
        q = ans1
        ans1 = ans2
        ans2 = (right_rectangle(fx, a+hs, b, hv) + q)/2
        if parity:
            hv = hv / 2
        parity = not parity
    return ans2
