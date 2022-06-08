import math


def main(y):
    result = 0
    a = 83 * pow(y, 3) + 73 * y + pow(y, 2) / 81
    b = pow(y, 1/2)
    c = pow(y, 2) / 63
    if y < 114:
        result = 49 * pow(a, 3)
    elif 114 <= y < 193:
        result = pow(b, 7) - 18 * pow(y, 4) - pow(math.cos(y), 2)
    elif 193 <= y < 247:
        result = pow(y, 5) + pow(60*y - 1, 4) + 90 * pow(y, 6)
    elif y >= 247:
        result = pow(c, 3)

    return result

print(main(133))  # 4.25e+06
print(main(216))  # 1.40e+06