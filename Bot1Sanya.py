import math


def int_r(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num


def main(z, x, y):
    step1 = 44 * pow(z, 3) - 52*x - 1
    step2 = pow(math.atan(step1), 7)
    result = step2/90

    step3 = 29 * pow(y, 5)
    step4 = 1 + 75 * pow(x, 2) + pow(y, 3)
    step5 = pow(step4, 5)
    step6 = 55 * pow(z, 2) / 26
    result += step3 + step5 + step6

    return result


print(main(0.66, -0.3, -0.38))
print(main(-0.37, 0.28, -0.47))
