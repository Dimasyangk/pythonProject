import math


def main(n, m, b):
    res2 = 1
    for i in range(1, m+1):
        res1 = 0
        for k in range(1, n+1):
            res1 += (i**5 + 96 * (16 + 47*(k**2))**6)
        res2 *= res1
    res3 = 0
    for j in range(1, n+1):
        for k1 in range(1, b+1):
            res3 += (33+86*j+93*k**3)**3
    a = res2 - res3
    a = "{:.2e}".format(a)
    return a


if __name__ == "__main__":
    print(main(4, 4, 2),
          main(3, 5, 8),
          main(2, 8, 8),
          main(6, 5, 6),
          main(3, 2, 4))
