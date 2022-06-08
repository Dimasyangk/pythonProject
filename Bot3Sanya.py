import math


def main(n, m, b, p):
    sum1 = 0
    for i in range(1, b + 1):
        for k in range(1, m + 1):
            for j in range(1, n + 1):
                num1 = 14*(math.ceil(p))**6
                num2 = (32*i - 55*j**2)**3 + 26*k
                sum1 += (num1 + num2)

    return sum1


print(main(8, 7, 4, 0.56))
print(main(2, 3, 7, 0.92))
