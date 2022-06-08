import math


def int_r(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num


def main(y, x):
    step1 = 48 * pow((x / 50) - 0.02, 6)
    step2 = 36 * pow(math.cos(y), 7)
    result = step1 + step2

    step3 = (10 * pow(y, 2) - y - 0.01)
    step4 = 77 * pow(step3, 3)
    step5 = x + 18 * pow(x, 2)
    step6 = 19 * pow(math.sin(step5), 6)
    step7 = step4 - step6
    result /= step7

    step8 = pow(y, 2)
    step9 = 22 * pow(21 * step8, 1/2) + pow(x, 6)
    step10 = pow(step9, 1/2)
    result -= step10

    return result


print(main(-0.55, 0.39))
print(main(-0.95, 0.74))
