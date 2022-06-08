def fast_pow(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a

    result = 0
    b1 = a