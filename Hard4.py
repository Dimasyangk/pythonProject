import math


def main(n):
    if n == 0:
        return -0.08
    elif n >= 1:
        step1 = (main(n-1) ** 2)/84
        step2 = (main(n-1) ** 3)/50 + 0.01
        step3 = (35 * main(n-1) ** 2)**2
        return 5 * math.sqrt(step1+step2)**3 + step3


if __name__ == "__main__":
    print(main(3),
          main(1),
          main(8),
          main(5),
          main(2))
