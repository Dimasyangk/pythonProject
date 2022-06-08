import math


def main(y):
    result = 0
    a = 80 * pow(y, 3) - pow(y, 2) - 44*y
    if y < -34:
        result = pow(y, 3) + pow(y, 8)
    elif -34 <= y < 15:
        result = 55 * pow(y, 2) - math.tan(y) - 82 * (pow(math.atan(a), 7))
    elif 15 <= y < 28:
        result = 54 * pow(y, 2) / 93
    elif y >= 28:
        result = pow(y, 6) + 51 + 49 * pow(y, 4)

    return result

print(main(-54))  # 4.25e+06
print(main(3))  # 1.40e+06