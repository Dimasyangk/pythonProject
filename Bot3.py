import math


def main(b, y, n):
    sum1 = 0
    for k in range(1, b + 1):
        sum1 += 31 * (math.floor(y)) ** 2 - 65*k**6 - (1 - 23 * k ** 3) ** 5

    sum2 = 0
    for k1 in range(1, n + 1):
        res1 = 52 * y ** 2 - 44 * k1 - y ** 3 / 39
        res2 = 70 * pow(math.sin(res1), 5)
        sum2 += res2

    return sum1 - sum2


print(main(4, -0.18, 7))
print(main(7, 1.0, 7))
