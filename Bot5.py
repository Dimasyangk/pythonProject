from math import *


def main(z, y):
    n = len(z)
    res = 0.0
    for i in range(1, n + 1):
        num1 = y[n - ceil(i/4)] + 1 + z[ceil(i/3)-1] ** 3
        num2 = log10(num1)**4
        res += num2
    return res * 73


print(main([-0.05, 0.04, -0.68, 0.26], [-0.26, -0.21, -0.03, 0.4]))
print(main([-0.33, 0.13, 0.97, 0.22], [-0.8, -0.71, 0.48, -0.67]))
