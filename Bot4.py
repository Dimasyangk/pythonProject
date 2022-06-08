import math


def main(n):
    if n == 0:
        return 0.40
    if n == 1:
        return -0.44
    elif n >= 2:
        return math.cos(80*main(n - 1) + main(n - 1)**2 + main(n - 2)**3) + 1


print(main(6))
print(main(7))